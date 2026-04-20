from pydantic import BaseModel, Field
from typing import Dict, Any, List
import time
import uuid

class TraceSpan(BaseModel):
    span_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    start_time: float = Field(default_factory=time.time)
    end_time: float = 0.0
    metadata: Dict[str, Any] = {}

class ExecutionTrace(BaseModel):
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    request_prompt: str
    spans: List[TraceSpan] = []
    overall_latency_ms: float = 0.0
