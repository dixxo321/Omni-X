import pytest
from omnimesh_x.agents.executive import ExecutiveAgent
from omnimesh_x.schemas.api import TaskRequest

@pytest.mark.asyncio
async def test_executive_mission():
    agent = ExecutiveAgent()
    req = TaskRequest(prompt="Execute core diagnostic routine", use_tools=True)
    response = await agent.run_mission(req)
    
    assert response.content == "Mission verified and complete. All subtasks executed within bounds."
    assert response.provider_used == "executive_swarm_v1"
    assert response.metadata.get("plan_depth") > 0
    assert response.trace_id is not None
