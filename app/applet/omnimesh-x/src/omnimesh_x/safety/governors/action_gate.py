class ActionGate:
    def __init__(self, risk_tolerance_level: int = 1):
        self.risk_tolerance_level = risk_tolerance_level

    def evaluate(self, tool_name: str, args: dict) -> bool:
        # Prevent execution of dangerous tools outside local secure boundary
        if tool_name == "bash" and self.risk_tolerance_level < 3:
            return False
        return True
