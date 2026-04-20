from pydantic import BaseModel
from typing import Any, Dict

class ToolRequest(BaseModel):
    tool_name: str
    arguments: Dict[str, Any]

class ToolResponse(BaseModel):
    status: str
    result: Any
