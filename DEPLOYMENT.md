# Deployment Guide for Superagent SDK Demo

This guide explains how to deploy the Superagent Python SDK demo application to Render.

## Overview

This repository contains:
1. **Superagent Python SDK** - The core SDK for interacting with Superagent API
2. **Demo Web Application** - A FastAPI application showcasing the SDK functionality

## Important: Two Deployment Options

### Option 1: Using Superagent Cloud (Recommended for Demo)
Deploy just the demo application that connects to Superagent's hosted API.

### Option 2: Full Superagent Deployment
Deploy the complete Superagent framework with all dependencies.

## Prerequisites

### For Option 1 (Superagent Cloud):
1. A Render account
2. A Superagent API token from [Superagent Cloud](https://superagent.sh)

### For Option 2 (Full Deployment):
1. A Render account
2. PostgreSQL database (Render PostgreSQL or external)
3. Vector database (Qdrant, Pinecone, etc.)
4. LLM provider API keys (OpenAI, Anthropic, etc.)

## Required Environment Variables

### Option 1: Superagent Cloud Demo (Minimal Setup)

**Required:**
- `SUPERAGENT_API_TOKEN` - Your Superagent Cloud API token

**Optional:**
- `SUPERAGENT_BASE_URL` - API base URL (defaults to `https://api.beta.superagent.sh`)
- `PORT` - Server port (Render sets automatically)

### Option 2: Full Superagent Deployment (Complete Setup)

**Core Requirements:**
- `SUPERAGENT_API_TOKEN` - Your API token for the demo app
- `OPENAI_API_KEY` - OpenAI API key (required for most operations)
- `DATABASE_URL` - PostgreSQL connection string with pooling
- `DATABASE_MIGRATION_URL` - PostgreSQL connection without pooling
- `JWT_SECRET` - Secret key for authentication
- `VECTORSTORE` - Vector database type (qdrant, pinecone, weaviate, etc.)

**Vector Database (choose one):**
- **Qdrant:** `QDRANT_API_KEY`, `QDRANT_HOST`, `QDRANT_INDEX`
- **Pinecone:** `PINECONE_API_KEY`, `PINECONE_ENVIRONMENT`, `PINECONE_INDEX`
- **Weaviate:** `WEAVIATE_URL`, `WEAVIATE_API_KEY`

**Additional LLM Providers (optional):**
- `ANTHROPIC_API_KEY` - For Claude models
- `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` - For Azure OpenAI
- `HUGGINGFACE_API_KEY` - For Hugging Face models
- `GROQ_API_KEY` - For Groq models
- `MISTRAL_API_KEY` - For Mistral models
- `COHERE_API_KEY` - For Cohere models

**Observability (optional):**
- `AGENTOPS_API_KEY` - For AgentOps monitoring
- `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY` - For Langfuse tracing

**Tools & Integrations (optional):**
- `E2B_API_KEY` - For code interpreter
- `REPLICATE_API_TOKEN` - For Replicate models

## Deployment Steps

### Option 1: Using render.yaml (Recommended)

1. Fork/clone this repository
2. Connect your GitHub repository to Render
3. Render will automatically detect the `render.yaml` file
4. Set the `SUPERAGENT_API_TOKEN` environment variable in the Render dashboard
5. Deploy!

### Option 2: Manual Setup

1. Create a new Web Service in Render
2. Connect your repository
3. Configure the following settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Health Check Path**: `/health`
4. Add environment variables (see above)
5. Deploy

## Files Added for Deployment

The following files were added to make this SDK deployable as a web application:

- `app.py` - FastAPI web application demonstrating the SDK
- `requirements.txt` - Python dependencies for deployment
- `render.yaml` - Render deployment configuration
- `static/index.html` - Web interface for testing the SDK
- `.env.example` - Example environment variables
- `DEPLOYMENT.md` - This deployment guide

## API Endpoints

Once deployed, the application provides:

- `GET /` - Web interface for testing the SDK
- `GET /health` - Health check endpoint
- `POST /agents` - Create a new agent
- `GET /agents` - List all agents
- `POST /agents/invoke` - Send a message to an agent

## Testing the Deployment

1. Visit your deployed URL
2. The web interface will load automatically
3. Click "Check API Health" to verify the configuration
4. Try creating an agent and sending messages

## Security Notes

- Never commit your `SUPERAGENT_API_TOKEN` to version control
- The demo application allows CORS from all origins - restrict this in production
- Consider adding authentication for production use

## Troubleshooting

### Common Issues

1. **"SUPERAGENT_API_TOKEN environment variable is required"**
   - Ensure you've set the API token in Render's environment variables

2. **"Configuration error"**
   - Check that your API token is valid
   - Verify the base URL is correct

3. **Import errors**
   - Ensure all dependencies are listed in `requirements.txt`
   - Check that the build command completed successfully

### Logs

Check the Render logs for detailed error information:
1. Go to your service in the Render dashboard
2. Click on "Logs" to see real-time application logs

## Development

To run locally:

1. Copy `.env.example` to `.env` and fill in your API token
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Visit `http://localhost:8000`

## Support

For issues with:
- **The SDK**: Check the [Superagent documentation](https://docs.superagent.sh)
- **Deployment**: Check Render's documentation or this guide
- **The demo app**: Review the application logs and API responses