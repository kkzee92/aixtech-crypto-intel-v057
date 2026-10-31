"""Multi-hash sealed lineage. Research only."""
import hashlib

def seal(data: str) -> dict:
    h256 = hashlib.sha256(data.encode()).hexdigest()
    h3 = hashlib.sha3_256(data.encode()).hexdigest()
    return {"sha256": h256, "sha3_256": h3, "sealed": True}
