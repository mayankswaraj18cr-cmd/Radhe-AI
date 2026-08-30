class GyanoAI:
    def __init__(self, name):
        self.name = name

    def respond(self, prompt):
        return {"persona": self.name, "prompt": prompt}
