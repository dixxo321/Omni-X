import subprocess
from ..tools.contracts import ToolRequest, ToolResponse

class BashTool:
    """
    Action-gated shell execution environment.
    Must be routed through the ActionGate governor to ensure risk < 3.
    """
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.forbidden_commands = ["rm -rf", "mkfs", "chown", "chmod"]

    def execute(self, request: ToolRequest) -> ToolResponse:
        command = request.arguments.get("command", "")
        
        for forbidden in self.forbidden_commands:
            if forbidden in command:
                return ToolResponse(status="blocked", result="Safety violation: Forbidden command pattern.")
                
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True, timeout=self.timeout
            )
            return ToolResponse(status="success", result=result.stdout or result.stderr)
        except subprocess.TimeoutExpired:
            return ToolResponse(status="timeout", result="")
        except Exception as e:
            return ToolResponse(status="error", result=str(e))
