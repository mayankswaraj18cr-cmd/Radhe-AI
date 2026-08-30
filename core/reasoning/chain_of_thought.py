class ChainOfThought:
    def __init__(self):
        self.trace = []

    def generate(self, prompt):
        self.trace = [
            "Understand the user request",
            "Gather evidence or context",
            "Critically reason and answer",
        ]
        return {"prompt": prompt, "trace": self.trace}
