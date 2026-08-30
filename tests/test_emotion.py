from core.emotion.tone_calibration import ToneCalibrator


def test_tone_calibration_returns_profile():
    calibrator = ToneCalibrator()
    profile = calibrator.calibrate("friendly")
    assert "tone" in profile
    assert "intensity" in profile
