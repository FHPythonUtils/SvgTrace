"""Test the image tracer."""

import asyncio
import sys
from pathlib import Path

import imgcompare
import pytest
from nocairosvg import svg2bitmap
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
logoFile = f"{THISDIR}/data/logo"
notExistsFile = f"{THISDIR}/data/notExists"

from svgtrace import asyncTrace, skimageTrace, trace


def aux_comparesvg(svgpath: str, pngpath: str) -> bool:
	output = f"{THISDIR}/data/{pngpath}"
	svg2bitmap(url=svgpath, write_to=output)
	imgcompare.is_equal(output.replace("-actual", "-expected"), output, tolerance=0.2)


def test_bw():
	Path(f"{logoFile}-bw.svg").write_text(trace(f"{logoFile}-bw.png", True), encoding="utf-8")
	aux_comparesvg(f"{logoFile}-bw.svg", "logo-actual-bw.png")


def test_colour():
	Path(f"{logoFile}.svg").write_text(trace(f"{logoFile}.png"), encoding="utf-8")
	aux_comparesvg(f"{logoFile}.svg", "logo-actual.png")


def test_asyncBw():
	Path(f"{logoFile}-asyncBw.svg").write_text(
		asyncio.run(asyncTrace(f"{logoFile}-bw.png", True)), encoding="utf-8"
	)
	aux_comparesvg(f"{logoFile}-asyncBw.svg", "logo-actual-bw.png")


def test_asyncColour():
	Path(f"{logoFile}-async.svg").write_text(
		asyncio.run(asyncTrace(f"{logoFile}.png")), encoding="utf-8"
	)
	aux_comparesvg(f"{logoFile}-async.svg", "logo-actual.png")


def test_skimageBw():
	Path(f"{logoFile}-skimagebw.svg").write_text(
		skimageTrace(Image.open(f"{logoFile}-bw.png")), encoding="utf-8"
	)
	aux_comparesvg(f"{logoFile}-skimagebw.svg", "logo-actual-skimagebw.png")


def test_skimageColour():
	Path(f"{logoFile}-skimage.svg").write_text(
		skimageTrace(Image.open(f"{logoFile}.png")), encoding="utf-8"
	)
	aux_comparesvg(f"{logoFile}-skimage.svg", "logo-actual-skimage.png")


def test_notExists():
	with pytest.raises(FileNotFoundError):
		Path(f"{notExistsFile}.svg").write_text(trace(f"{notExistsFile}.png"), encoding="utf-8")
