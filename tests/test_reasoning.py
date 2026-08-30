from core.reasoning.confidence_scoring import ConfidenceScorer


def test_confidence_score_ranges():
    scorer = ConfidenceScorer()
    assert 0.0 <= scorer.score("This is a strong answer") <= 1.0
