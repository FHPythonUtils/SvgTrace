"""Test the image tracer."""
import sys
from pathlib import Path

import imgcompare
import pytest
from nocairosvg import svg2bitmap

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
logoFile = f"{THISDIR}/data/logo"
notExistsFile = f"{THISDIR}/data/notExists"

from svgtrace import trace


def aux_comparesvg(svgpath: str, pngpath: str):
	output = f"{THISDIR}/data/{pngpath}"
	svg2bitmap(url=svgpath, write_to=output)
	imgcompare.is_equal(
		output.replace("-expected", "-actual"), f"{THISDIR}/data/{pngpath}", tolerance=0.2
	)


def test_bw():
	Path(f"{logoFile}-bw.svg").write_text(trace(f"{logoFile}-bw.png", True), encoding="utf-8")
	aux_comparesvg(f"{logoFile}-bw.svg", "logo-actual-bw.png")


def test_colour():
	Path(f"{logoFile}.svg").write_text(trace(f"{logoFile}.png"), encoding="utf-8")
	aux_comparesvg(f"{logoFile}.svg", "logo-actual.png")


def test_notExists():
	with pytest.raises(FileNotFoundError):
		Path(f"{notExistsFile}.svg").write_text(trace(f"{notExistsFile}.png"), encoding="utf-8")
