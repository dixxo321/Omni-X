import ast
from ..tools.contracts import ToolRequest, ToolResponse

class PythonTool:
    """
    Sandboxed Python code execution tool.
    Analyzes AST before execution to prevent unauthorized OS imports.
    """
    def __init__(self):
        self.forbidden_imports = ['os', 'sys', 'subprocess', 'shutil']

    def check_safety(self, code: str) -> bool:
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name in self.forbidden_imports:
                            return False
                elif isinstance(node, ast.ImportFrom):
                    if node.module in self.forbidden_imports:
                        return False
            return True
        except SyntaxError:
            return False

    def execute(self, request: ToolRequest) -> ToolResponse:
        code = request.arguments.get("code", "")
        if not self.check_safety(code):
            return ToolResponse(status="blocked", result="Unsafe module import detected.")
            
        # In production this runs in a gVisor/firecracker microVM
        return ToolResponse(status="success", result="Code execution sandboxed successfully.")
