from pydantic import BaseModel
from typing import Optional, Dict, Any

class TaskRequest(BaseModel):
    prompt: str
    task_type: Optional[str] = "general"
    use_tools: bool = False
    context: Optional[str] = None

class TaskResponse(BaseModel):
    content: str
    provider_used: str
    trace_id: str
    metadata: Dict[str, Any] = {}
