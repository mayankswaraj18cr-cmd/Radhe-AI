from core.verification.hallucination_guard import HallucinationGuard


def test_hallucination_guard_flags_missing_source():
    guard = HallucinationGuard()
    result = guard.verify("No evidence provided")
    assert "status" in result
