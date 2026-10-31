from crypto_intel.security.redact import redact
from crypto_intel.security.audit import seal

def test_redact():
    assert "[REDACTED]" in redact("seed phrase example here")

def test_seal():
    s = seal("test")
    assert "sha256" in s and s["sealed"]
