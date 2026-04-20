from fastapi import FastAPI
from ..schemas.api import TaskRequest, TaskResponse
from ..routing.router import Router

app = FastAPI(title="OmniMesh X API", version="0.1.0")
router = Router()

@app.post("/v1/generate", response_model=TaskResponse)
async def generate(request: TaskRequest):
    # Flow: Receive request -> Route / Evaluate constraints -> Execute -> Return payload
    response = await router.route_and_execute(request)
    return response

@app.get("/health")
async def health():
    return {"status": "operational", "system": "OmniMesh X Kernel"}
