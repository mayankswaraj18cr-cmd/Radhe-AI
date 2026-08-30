class TransparentReasoning:
    def __init__(self):
        self.steps = []

    def explain(self, claim):
        self.steps = ["Parse intent", "Reason over evidence", "Synthesize answer"]
        return {"claim": claim, "steps": self.steps}
