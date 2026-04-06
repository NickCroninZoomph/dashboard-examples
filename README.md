# Powerpoint Generator — static dashboards

Two self-contained HTML dashboards (Chart.js + embedded JSON). No build step.

**Repository:** [github.com/NickCroninZoomph/dashboard-examples](https://github.com/NickCroninZoomph/dashboard-examples)

## GitHub Pages

1. In this folder, connect and push (if you haven’t already):

   ```bash
   cd "/Users/nickcronin/Desktop/Powerpoint Generator"
   git remote add origin https://github.com/NickCroninZoomph/dashboard-examples.git
   git push -u origin main
   ```

   If `origin` already exists:

   ```bash
   git remote set-url origin https://github.com/NickCroninZoomph/dashboard-examples.git
   git push -u origin main
   ```

2. **Turn on GitHub Pages** — **Settings → Pages** → under **Build and deployment**:

   - **Recommended:** set **Source** to **GitHub Actions** (this repo includes `.github/workflows/pages.yml`). After you push, open the **Actions** tab and wait for **Deploy GitHub Pages** to finish (green).
   - If you prefer **Deploy from a branch** instead: branch **main**, folder **/ (root)** → Save.

   If the site still shows **404**, use **GitHub Actions** only (not both).

3. Live site (after the workflow succeeds or the branch deploy finishes):

   - **Home:** [nickcroninzoomph.github.io/dashboard-examples/](https://nickcroninzoomph.github.io/dashboard-examples/)
   - **NBA:** […/nba-prime-dashboard/](https://nickcroninzoomph.github.io/dashboard-examples/nba-prime-dashboard/)
   - **Invisalign NFL:** […/invisalign-nfl-dashboard/](https://nickcroninzoomph.github.io/dashboard-examples/invisalign-nfl-dashboard/)

## Updating data

Edit the `window.NBA_DASHBOARD_DATA` or `window.INV` JSON inside each `index.html`, commit, and push.
