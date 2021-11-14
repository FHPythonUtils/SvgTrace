"""Test the image tracer."""

from pathlib import Path

from svgtrace import trace

THISDIR = str(Path(__file__).resolve().parent)


Path(f"{THISDIR}/logo-bw.svg").write_text(trace(THISDIR + "/logo-bw.png", True), encoding="utf-8")

Path(f"{THISDIR}/logo.svg").write_text(trace(THISDIR + "/logo.png"), encoding="utf-8")
