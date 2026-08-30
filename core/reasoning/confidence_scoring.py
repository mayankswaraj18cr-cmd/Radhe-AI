class ConfidenceScorer:
    def score(self, text):
        quality = min(max(len(text) / 250.0, 0.0), 1.0)
        return round(quality, 3)
