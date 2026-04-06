# Powerpoint Generator — static dashboards

Two self-contained HTML dashboards (Chart.js + embedded JSON). No build step.

**GitHub account:** [NickCroninZoomph](https://github.com/NickCroninZoomph)

## GitHub Pages

1. Create a **new repository** under your account (e.g. `powerpoint-generator` or `dashboards`).

2. In this folder on your machine (this repo is already initialized with `main`):

   ```bash
   cd "/Users/nickcronin/Desktop/Powerpoint Generator"
   git remote add origin https://github.com/NickCroninZoomph/YOUR_REPO_NAME.git
   git push -u origin main
   ```

   Replace `YOUR_REPO_NAME` with the repo you created. If `git remote add` fails because `origin` exists, use `git remote set-url origin https://github.com/NickCroninZoomph/YOUR_REPO_NAME.git` instead.

3. On GitHub: **Settings → Pages** (under “Code and automation”).

4. Under **Build and deployment → Source**, choose **Deploy from a branch**.

5. Branch: **main**, folder: **/ (root)** → Save.

6. After a minute, the site is at:

   `https://nickcroninzoomph.github.io/YOUR_REPO_NAME/`

   (GitHub lowercases the username in Pages URLs.)

   Direct links:

   - `https://nickcroninzoomph.github.io/YOUR_REPO_NAME/nba-prime-dashboard/`
   - `https://nickcroninzoomph.github.io/YOUR_REPO_NAME/invisalign-nfl-dashboard/`

## Updating data

Edit the `window.NBA_DASHBOARD_DATA` or `window.INV` JSON inside each `index.html`, commit, and push.
