# Powerpoint Generator — static dashboards

Self-contained HTML dashboards (Chart.js + embedded JSON). No build step — **NBA on Prime**, **Invisalign NFL**, and **Portland Thorns FC**.

**Repository:** [github.com/NickCroninZoomph/dashboard-examples](https://github.com/NickCroninZoomph/dashboard-examples)

**Site files live in `docs/`** so GitHub Pages can use **main** + **/docs** (the most reliable setup).

## GitHub Pages — do these in order

1. Push the latest `main`:

   ```bash
   cd "/Users/nickcronin/Desktop/Powerpoint Generator"
   git push origin main
   ```

2. Open **Settings → Pages** for the repo:  
   `https://github.com/NickCroninZoomph/dashboard-examples/settings/pages`

3. Under **Build and deployment**:
   - **Source:** **Deploy from a branch**
   - **Branch:** **`main`** (not `gh-pages`)
   - **Folder:** **`/docs`**
   - Click **Save**

4. Wait until the banner says something like **“Your site is live at …”** (can take 2–5 minutes the first time).

5. Open:

   - **Home:** https://nickcroninzoomph.github.io/dashboard-examples/
   - **NBA:** https://nickcroninzoomph.github.io/dashboard-examples/nba-prime-dashboard/
   - **Invisalign:** https://nickcroninzoomph.github.io/dashboard-examples/invisalign-nfl-dashboard/
   - **Thorns:** https://nickcroninzoomph.github.io/dashboard-examples/thorns-dashboard/

If you still see 404, the Pages source is almost always still wrong — double-check it says **`main`** and **`/docs`**, not **`/ (root)`** on `main`.

## Updating data

Edit the JSON inside:

- `docs/nba-prime-dashboard/index.html` (`window.NBA_DASHBOARD_DATA`)
- `docs/invisalign-nfl-dashboard/index.html` (`window.INV`)
- `docs/thorns-dashboard/index.html` (`window.THORNS_DASHBOARD_DATA`)

Then commit and push `main`.
