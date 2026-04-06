# Powerpoint Generator — static dashboards

Two self-contained HTML dashboards (Chart.js + embedded JSON). No build step.

## GitHub Pages

1. Create a **new repository** on GitHub (e.g. `dashboards` or `powerpoint-generator`).

2. In this folder on your machine:

   ```bash
   cd "/Users/nickcronin/Desktop/Powerpoint Generator"
   git init
   git add index.html README.md .gitignore nba-prime-dashboard invisalign-nfl-dashboard
   git commit -m "Add dashboards for GitHub Pages"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

   Replace `YOUR_USERNAME` and `YOUR_REPO` with your GitHub user and repo name.

3. On GitHub: **Settings → Pages** (under “Code and automation”).

4. Under **Build and deployment → Source**, choose **Deploy from a branch**.

5. Branch: **main**, folder: **/ (root)** → Save.

6. After a minute, the site is at:

   `https://YOUR_USERNAME.github.io/YOUR_REPO/`

   Direct links:

   - `https://YOUR_USERNAME.github.io/YOUR_REPO/nba-prime-dashboard/`
   - `https://YOUR_USERNAME.github.io/YOUR_REPO/invisalign-nfl-dashboard/`

## Updating data

Edit the `window.NBA_DASHBOARD_DATA` or `window.INV` JSON inside each `index.html`, commit, and push.
