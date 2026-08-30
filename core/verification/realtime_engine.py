class RealtimeEngine:
    def __init__(self):
        self.sources = []

    def update(self, source):
        self.sources.append(source)
        return self.sources
