from crypto_intel.strategies.asset_class import score_signal

def test_score_stress():
    assert score_signal("major", "stress", {}) == 0.0

def test_score_basic():
    s = score_signal("major", "trend", {"strength": 0.6})
    assert 0 < s <= 0.08
