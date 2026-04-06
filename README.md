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

2. **Publish & turn on Pages**

   - Push `main` (the workflow `.github/workflows/pages.yml` copies the dashboards into a `site/` folder and pushes that to branch **`gh-pages`**).
   - **Actions** tab → wait until **Publish site to gh-pages** is green.
   - **Settings → Pages** → **Build and deployment** → **Source:** **Deploy from a branch** → Branch **`gh-pages`**, folder **`/ (root)`** → Save.

   (Using branch **`gh-pages`** avoids the newer “deploy-pages” setup that often stays on 404.)

3. Live site (give it 1–2 minutes after the workflow succeeds):

   - **Home:** [nickcroninzoomph.github.io/dashboard-examples/](https://nickcroninzoomph.github.io/dashboard-examples/)
   - **NBA:** […/nba-prime-dashboard/](https://nickcroninzoomph.github.io/dashboard-examples/nba-prime-dashboard/)
   - **Invisalign NFL:** […/invisalign-nfl-dashboard/](https://nickcroninzoomph.github.io/dashboard-examples/invisalign-nfl-dashboard/)

## Updating data

Edit the `window.NBA_DASHBOARD_DATA` or `window.INV` JSON inside each `index.html`, commit, and push.
