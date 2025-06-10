# 🚀 Render Deployment Guide

## Quick Deploy to Render

This repository is ready for one-click deployment to Render.

### Step 1: Connect Repository
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository: `TradieMate/superagent-py`

### Step 2: Configure Deployment
Render will automatically detect the `render.yaml` configuration file.

### Step 3: Set Environment Variable
In the Render dashboard, add this environment variable:

```
SUPERAGENT_API_TOKEN = your_actual_superagent_api_token
```

**Get your token from:** [Superagent Cloud](https://superagent.sh)

### Step 4: Deploy
Click "Deploy" - Render will:
- Install dependencies from `requirements.txt`
- Start the FastAPI application
- Make it available at your Render URL

## What Gets Deployed

- **FastAPI Web Application** with demo interface
- **Health check endpoint** at `/health`
- **API endpoints** for testing Superagent SDK
- **Static web interface** for easy testing

## After Deployment

1. Visit your Render URL
2. Use the web interface to test the Superagent SDK
3. Check `/health` endpoint for monitoring

## Environment Variables

### Required:
- `SUPERAGENT_API_TOKEN` - Your Superagent API token

### Optional (have defaults):
- `SUPERAGENT_BASE_URL` - Defaults to `https://api.beta.superagent.sh`
- `PORT` - Render sets this automatically

## Troubleshooting

### If deployment fails:
1. Check Render logs for errors
2. Verify `SUPERAGENT_API_TOKEN` is set correctly
3. Ensure token has proper permissions

### If app doesn't respond:
1. Check health endpoint: `https://your-app.onrender.com/health`
2. Review application logs in Render dashboard

## Support

- **Render Issues**: Check [Render Documentation](https://render.com/docs)
- **Superagent Issues**: Check [Superagent Documentation](https://docs.superagent.sh)

---

**That's it!** Your Superagent Python SDK demo is now running on Render. 🎉