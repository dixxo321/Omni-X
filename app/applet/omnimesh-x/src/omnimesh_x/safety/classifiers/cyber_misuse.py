class CyberMisuseClassifier:
    def __init__(self):
        self.blocked_keywords = ["exploit", "cve", "0day", "ransomware_payload", "rootkit"]

    def analyze(self, prompt: str) -> dict:
        prompt_lower = prompt.lower()
        for kw in self.blocked_keywords:
            if kw in prompt_lower:
                return {"is_safe": False, "reason": f"Detected restricted cyber terminology: {kw}"}
        return {"is_safe": True, "reason": "No policy violations detected"}
