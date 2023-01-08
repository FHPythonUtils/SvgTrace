"""Author FredHappyface 2020.

Uses playwright to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below
"""
from __future__ import annotations

import asyncio
from pathlib import Path

from install_playwright import install
from playwright.sync_api import sync_playwright


THISDIR = str(Path(__file__).resolve().parent)




def trace(filename: str, blackAndWhite: bool = False, mode: str = "default") -> str:
	"""Do a trace of an image on the filesystem using the playwright library.

	Args:
		filename (str): The location of the file on the filesystem, use an
		absolute filepath for this
		blackAndWhite (bool, optional): Trace a black and white SVG. Defaults to False.
		mode (str, optional): Set the mode. See https://github.com/jankovicsandras/imagetracerjs
		for more information. Defaults to "default".

	Returns:
		str: SVG string
	"""
	if mode.find("black") >= 0 or blackAndWhite:
		mode = "posterized1"

	filename=filename.replace('\\', '/')

	with sync_playwright() as p:
		install(p.chromium)
		browser = p.chromium.launch(
			args=["--no-sandbox", "--disable-web-security", "--allow-file-access-from-files"]
		)

		page = browser.new_page()
		page.goto(f"file:///{THISDIR}/imagetracer.html")
		page.evaluate(
			f"ImageTracer.imageToSVG('file:///{filename}',function(svgstr){{ ImageTracer.appendSVGString( svgstr, 'svg-container' ); }},'{mode}');"
		)
		element = page.query_selector("div")
		svg = page.evaluate("(element) => element.innerHTML", element)

		browser.close()
	return svg
