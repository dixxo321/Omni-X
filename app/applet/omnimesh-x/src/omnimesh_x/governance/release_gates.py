from ..evals.harness import EvalHarness

class ReleaseController:
    def __init__(self, threshold: float = 0.85):
        self.eval_harness = EvalHarness()
        self.threshold = threshold

    def check_release_readiness(self, version: str) -> bool:
        results = self.eval_harness.run_suite(version)
        for metric, score in results["scores"].items():
            if score < self.threshold:
                return False
        return True
