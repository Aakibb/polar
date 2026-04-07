# Sokrio Task and PJP Planner

A static website containing project overview and activity planning documentation.

## Deployment to Railway

This project is configured for deployment on Railway as a static website.

### Prerequisites
- Railway account
- Git repository

### Deployment Steps

1. **Push to GitHub/GitLab**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Create Railway Project**
   - Go to [Railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Automatic Deployment**
   - Railway will detect the `railway.json` configuration
   - It will install dependencies and start the `serve` server
   - Your site will be live at the provided Railway URL

### Configuration

- **railway.json**: Railway deployment configuration
- **package.json**: Node.js dependencies and start script
- **Start Command**: `npm start` (runs `serve .` to serve static files)

### Local Testing

Test locally before deploying:
```bash
npm install
npm start
```

Then open `http://localhost:3000` in your browser.

### Files Included

- `Project_Overview.html` - Main documentation page
- `daily-planner.html` - Daily planner interface
- `pjp-planner.html` - PJP planner interface
- `team-members.html` - Team management interface
- `activity-settings.html` - Activity configuration
- `holiday-settings.html` - Holiday settings
- `pjp-settings.html` - PJP settings
- `Project_Overview.md` - Source markdown documentation
- `build_pdf.py` - Local PDF generation script (optional)

### Notes

- The site serves static HTML files from the root directory
- All HTML files are directly accessible
- No database or backend required
- Free tier on Railway should be sufficient for this static site