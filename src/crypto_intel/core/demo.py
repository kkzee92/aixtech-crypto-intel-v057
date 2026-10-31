"""Demo runner for paper-only research."""
from crypto_intel.strategies.asset_class import score_signal

def run_demo():
    print("AIxTech crypto intel v0.57 - paper only demo")
    factors = {"strength": 0.7, "vol_tier": 0.4, "anomaly": 0.2, "correlation": 0.3}
    score = score_signal("major", "trend", factors)
    print(f"Sample major score: {score}")
    print("Research only. No live execution.")
