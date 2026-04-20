from ...schemas.api import TaskRequest
from typing import List, Dict

class ExecutionNode:
    def __init__(self, step_id: str, description: str, requires_tools: bool = False):
        self.step_id = step_id
        self.description = description
        self.requires_tools = requires_tools

class Planner:
    def create_plan(self, request: TaskRequest) -> List[ExecutionNode]:
        plan = []
        if request.use_tools:
            plan.append(ExecutionNode("step_1", "Gather context using tools", True))
        plan.append(ExecutionNode("step_2", "Synthesize findings and format response"))
        return plan
