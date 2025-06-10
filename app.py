"""
Superagent SDK Demo Web Application
A simple FastAPI application demonstrating the Superagent Python SDK
"""

import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

# Import the Superagent SDK
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from superagent.client import Superagent
from superagent.core.api_error import ApiError

app = FastAPI(
    title="Superagent SDK Demo",
    description="A demo web application showcasing the Superagent Python SDK",
    version="1.0.0"
)

# Enable CORS for all origins (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic models for request/response
class AgentCreateRequest(BaseModel):
    name: str
    description: str
    llm_model: str = "GPT_4_1106_PREVIEW"
    prompt: str = "You are a helpful assistant"
    is_active: bool = True

class AgentInvokeRequest(BaseModel):
    agent_id: str
    input: str
    session_id: str = "demo-session"
    enable_streaming: bool = False

class HealthResponse(BaseModel):
    status: str
    message: str

# Initialize Superagent client
def get_superagent_client():
    token = os.getenv("SUPERAGENT_API_TOKEN", "demo-token-not-configured")
    base_url = os.getenv("SUPERAGENT_BASE_URL", "https://api.beta.superagent.sh")
    
    return Superagent(token=token, base_url=base_url)

def check_token_configured():
    """Check if API token is properly configured"""
    token = os.getenv("SUPERAGENT_API_TOKEN")
    if not token or token == "demo-token-not-configured":
        raise HTTPException(
            status_code=400, 
            detail="SUPERAGENT_API_TOKEN not configured. Please set this environment variable in Render dashboard."
        )

@app.get("/")
async def root():
    """Serve the demo frontend"""
    return FileResponse("static/index.html")

@app.get("/api", response_model=HealthResponse)
async def api_root():
    """API health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="Superagent SDK Demo API is running"
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check"""
    return HealthResponse(
        status="healthy",
        message="Superagent SDK Demo is running"
    )

@app.post("/agents")
async def create_agent(request: AgentCreateRequest):
    """Create a new agent"""
    try:
        check_token_configured()
        client = get_superagent_client()
        agent = client.agent.create(request={
            "name": request.name,
            "description": request.description,
            "isActive": request.is_active,
            "llmModel": request.llm_model,
            "prompt": request.prompt
        })
        return {"success": True, "agent": agent.data}
    except ApiError as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agents/invoke")
async def invoke_agent(request: AgentInvokeRequest):
    """Invoke an agent with input"""
    try:
        check_token_configured()
        client = get_superagent_client()
        output = client.agent.invoke(
            agent_id=request.agent_id,
            input=request.input,
            enable_streaming=request.enable_streaming,
            session_id=request.session_id
        )
        return {"success": True, "output": output}
    except ApiError as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agents")
async def list_agents():
    """List all agents"""
    try:
        check_token_configured()
        client = get_superagent_client()
        agents = client.agent.list()
        return {"success": True, "agents": agents}
    except ApiError as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        access_log=True
    )