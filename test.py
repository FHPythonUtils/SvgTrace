""" Test the image tracer """

from pathlib import Path
from svgtrace import trace

THISDIR = str(Path(__file__).resolve().parent)

bw = open(THISDIR + "/logo-bw.svg", "w")
bw.write(trace(THISDIR + "/logo-bw.png", True))
bw.close()
colour = open(THISDIR + "/logo.svg", "w")
colour.write(trace(THISDIR + "/logo.png"))
colour.close()
