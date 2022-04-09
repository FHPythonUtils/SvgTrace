"""Test the image tracer."""
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
logoFile = f"{THISDIR}/data/logo"

from svgtrace import trace

Path(f"{logoFile}-bw.svg").write_text(trace(f"{logoFile}-bw.png", True), encoding="utf-8")

Path(f"{logoFile}.svg").write_text(trace(f"{logoFile}.png"), encoding="utf-8")
