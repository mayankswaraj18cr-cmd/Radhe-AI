class SessionMemory:
    def __init__(self):
        self.history = []

    def add(self, prompt, response):
        self.history.append({"prompt": prompt, "response": response})
        return self.history[-1]
