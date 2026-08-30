class HallucinationGuard:
    def verify(self, text):
        ok = bool(text and "evidence" in text.lower() or "source" in text.lower())
        return {"status": "pass" if ok else "warning", "verified": ok}
