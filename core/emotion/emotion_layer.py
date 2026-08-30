class EmotionLayer:
    def __init__(self):
        self.state = {"tone": "neutral", "energy": "medium"}

    def assess(self, input_text):
        return {"tone": "friendly" if "hello" in input_text.lower() else "neutral", "energy": "medium"}
