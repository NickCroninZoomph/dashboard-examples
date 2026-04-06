#!/usr/bin/env python3
"""
Extracts NBA on Prime social media analytics from the recap Excel file
and prints window.NBA_DASHBOARD_DATA = {...}; for embedding in index.html.

Usage:
    /opt/homebrew/bin/python3.13 extract_data.py > /tmp/data_block.js
    # Then paste the output into the <script> data block in index.html.

To use a different Excel file:
    EXCEL_PATH = "/path/to/new/recap.xlsx"
"""
import json
import datetime
import pandas as pd

EXCEL_PATH = "/Users/nickcronin/Downloads/nba on prime february 26 recap.xlsx"
GAME_DATE  = "February 26, 2026"
REPORT_TITLE = "NBA on Prime"

# ---------------------------------------------------------------------------
def load_sheets():
    sheets = pd.read_excel(EXCEL_PATH, sheet_name=None)
    prime = sheets["PRIME"]
    nbc   = sheets["NBC"]
    espn  = sheets["ESPN"]
    s4    = sheets["Sheet4"]   # platform-level summary (header in row 0)
    s5    = sheets["Sheet5"]   # week-over-week (no normal header)
    return prime, nbc, espn, s4, s5

# ---------------------------------------------------------------------------
def engagements_by_source(df):
    """Return engagements summed by platform for a given sheet."""
    sources = ["Twitter", "Instagram", "Facebook", "YouTube"]
    return [int(df[df["Source"] == s]["TotalPublicEngagements"].fillna(0).sum())
            for s in sources]

def weighted_er(s4_rows):
    """
    Post-weighted average engagement rate from a slice of Sheet4.
    Sheet4 columns: Source | AuthorDisplayName | Platform | Posts |
                    Engagements | Impressions | E/P | ER
    """
    posts_col = s4_rows["Posts"]
    er_col    = s4_rows["ER"]
    total_posts = posts_col.sum()
    if total_posts == 0:
        return 0.0
    return float((posts_col * er_col).sum() / total_posts) * 100

def top10(df):
    cols = ["Source", "ContentType", "Message",
            "TotalPublicEngagements", "VideoViews", "EngagementRate"]
    rows = df.nlargest(10, "TotalPublicEngagements")[cols]
    result = []
    for _, r in rows.iterrows():
        msg = str(r["Message"])
        # strip emoji safely — json ensure_ascii handles it, but truncate first
        if len(msg) > 90:
            msg = msg[:87] + "..."
        result.append({
            "platform":    str(r["Source"]),
            "contentType": str(r["ContentType"]),
            "message":     msg,
            "engagements": int(r["TotalPublicEngagements"]),
            "videoViews":  None if pd.isna(r["VideoViews"]) else int(r["VideoViews"]),
            "er":          round(float(r["EngagementRate"]) * 100, 2)
        })
    return result

# ---------------------------------------------------------------------------
def build():
    prime, nbc, espn, s4, s5 = load_sheets()

    # ── Sheet4 row slices ────────────────────────────────────────────────
    # Rows: 0=Twitter/Prime, 1=Instagram/Prime, 2=Facebook/Prime, 3=YouTube/Prime
    #       4=Twitter/NBC,   5=Instagram/NBC,   6=Facebook/NBC,   7=YouTube/NBC
    #       8=Twitter/ESPN,  9=Instagram/ESPN, 10=Facebook/ESPN, 11=YouTube/ESPN
    prime_s4 = s4.iloc[0:4]
    nbc_s4   = s4.iloc[4:8]
    espn_s4  = s4.iloc[8:12]

    # ── Prime KPIs ───────────────────────────────────────────────────────
    # Use Sheet4 for authoritative impression totals (IG/FB post-level = 0 in PRIME sheet)
    total_impressions = int(prime_s4["Impressions"].sum())
    total_engagements = int(prime_s4["Engagements"].sum())
    video_views       = int(prime["VideoViews"].fillna(0).sum())
    avg_er            = weighted_er(prime_s4)

    # ── Platform breakdown (Prime) ───────────────────────────────────────
    platforms = []
    for _, row in prime_s4.iterrows():
        platforms.append({
            "name":        str(row["Source"]),
            "posts":       int(row["Posts"]),
            "engagements": int(row["Engagements"]),
            "impressions": int(row["Impressions"]),
            "er":          round(float(row["ER"]) * 100, 2)
        })

    # ── Engagement breakdown (Prime) ─────────────────────────────────────
    fb_reactions = int(
        prime[["FBLoveCount", "FBHahaCount", "FBWowCount"]].fillna(0).sum().sum()
    )
    eng_breakdown = {
        "likes":          int(prime["LikeCount"].fillna(0).sum()),
        "comments":       int(prime["Comments"].fillna(0).sum()),
        "sharesRetweets": int(prime["Shares/Retweets"].fillna(0).sum()),
        "fbReactions":    fb_reactions,
    }

    # ── Content mix (Prime) ──────────────────────────────────────────────
    ct = prime["ContentType"].value_counts()
    total_posts_prime = len(prime)
    content_mix = [
        {"label": k, "count": int(v), "pct": round(v / total_posts_prime * 100, 2)}
        for k, v in ct.items()
    ]

    # ── Competitive totals ───────────────────────────────────────────────
    comp_totals_s4 = s4.iloc[0:12]  # all 12 platform rows
    # sheet4 has a summary block at far right: cols Platform.1/Posts.1/Engagements.1/Impressions.1
    competitors = []
    comp_meta = [
        ("Prime Video", prime_s4, "Prime"),
        ("NBC",         nbc_s4,   "NBC"),
        ("ESPN",        espn_s4,  "ESPN"),
    ]
    for name, rows, _ in comp_meta:
        er = weighted_er(rows)
        competitors.append({
            "name":        name,
            "posts":       int(rows["Posts"].sum()),
            "engagements": int(rows["Engagements"].sum()),
            "impressions": int(rows["Impressions"].sum()),
            "er":          round(er, 2),
        })

    # ── Competitive by platform ──────────────────────────────────────────
    by_platform = {
        "labels": ["Twitter", "Instagram", "Facebook", "YouTube"],
        "prime":  engagements_by_source(prime),
        "nbc":    engagements_by_source(nbc),
        "espn":   engagements_by_source(espn),
    }

    # ── Week-over-week (Sheet5) ──────────────────────────────────────────
    # Sheet5 has no header row — pandas reads col 0 as the header label.
    # The three periods are laid out horizontally:
    #   Cols 0-8 = Feb 26 (most recent), Cols 9-17 = Feb 19, Cols 18-25 = Feb 12
    # Row index 2 = Twitter, 3 = Instagram, 4 = Facebook, 5 = YouTube (platform rows)
    # We use the Sheet4 totals (already computed) as the authoritative period 1 values,
    # and parse Sheet5 for periods 2 and 3.

    # Sheet5 col layout per period (0-indexed within the period block):
    #   0=Source, 1=AuthorDisplayName, 2=Platform, 3=Posts, 4=Engagements, 5=Impressions, 6=E/P, 7=ER
    def wow_period_totals(col_offset):
        rows = s5.iloc[2:6]  # 4 platform rows
        try:
            posts       = int(rows.iloc[:, col_offset + 3].sum())
            engagements = int(rows.iloc[:, col_offset + 4].sum())
            impressions = int(rows.iloc[:, col_offset + 5].sum())
        except Exception:
            posts = engagements = impressions = 0
        return posts, engagements, impressions

    p1_posts, p1_eng, p1_imp = total_posts_prime, total_engagements, total_impressions  # Feb 26 (authoritative)
    p2_posts, p2_eng, p2_imp = wow_period_totals(9)    # Feb 19
    p3_posts, p3_eng, p3_imp = wow_period_totals(18)   # Feb 12

    week_over_week = {
        "periods":      ["Feb 12", "Feb 19", "Feb 26"],
        "posts":        [p3_posts, p2_posts, p1_posts],
        "engagements":  [p3_eng,   p2_eng,   p1_eng  ],
        "impressions":  [p3_imp,   p2_imp,   p1_imp  ],
    }

    # ── Assemble ─────────────────────────────────────────────────────────
    data = {
        "meta": {
            "reportTitle": REPORT_TITLE,
            "gameDate":    GAME_DATE,
            "lastUpdated": datetime.datetime.utcnow().strftime("%B %d, %Y at %I:%M %p UTC"),
            "source":      EXCEL_PATH.split("/")[-1],
        },
        "prime": {
            "kpi": {
                "totalEngagements": total_engagements,
                "totalImpressions": total_impressions,
                "videoViews":       video_views,
                "avgEngagementRate": round(avg_er, 2),
            },
            "platforms":           platforms,
            "engagementBreakdown": eng_breakdown,
            "contentMix":          content_mix,
        },
        "competitive": {
            "totals":     competitors,
            "byPlatform": by_platform,
        },
        "weekOverWeek": week_over_week,
        "topPosts":     top10(prime),
    }

    print("// TODO: replace with fetch('/api/nba-recap') for live data")
    print("window.NBA_DASHBOARD_DATA =", json.dumps(data, indent=2, ensure_ascii=True), ";")

if __name__ == "__main__":
    build()
