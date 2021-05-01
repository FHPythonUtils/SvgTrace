"""Test the image tracer."""

from pathlib import Path

from svgtrace import trace

THISDIR = str(Path(__file__).resolve().parent)


with open(THISDIR + "/logo-bw.svg", "w") as bw:
	bw.write(trace(THISDIR + "/logo-bw.png", True))

with open(THISDIR + "/logo.svg", "w") as colour:
	colour.write(trace(THISDIR + "/logo.png"))
