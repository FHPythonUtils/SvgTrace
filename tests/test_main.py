"""Test the image tracer."""
from pathlib import Path

from svgtrace import trace

THISDIR = str(Path(__file__).resolve().parent)
logoFile = f"{THISDIR}/data/logo"

Path(f"{logoFile}-bw.svg").write_text(trace(f"{logoFile}-bw.png", True), encoding="utf-8")

Path(f"{logoFile}.svg").write_text(trace(f"{logoFile}.png"), encoding="utf-8")
