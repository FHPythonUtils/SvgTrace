"""Author FredHappyface 2020.

Uses pyppeteer to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below
"""
from __future__ import annotations

import asyncio
from pathlib import Path

from pyppeteer import launch

THISDIR = str(Path(__file__).resolve().parent)


async def doTrace(filename: str, mode: str = "default"):
	"""Call web code."""
	browser = await launch(
		options={
			"args": [
				"--no-sandbox",
				"--headless",
				"--disable-web-security",
				"--allow-file-access-from-files",
			]
		}
	)
	page = await browser.newPage()
	await page.goto(f"file:///{THISDIR}/imagetracer.html")
	await page.evaluate(
		f"ImageTracer.imageToSVG('file:///{filename}',function(svgstr){{ ImageTracer.appendSVGString( svgstr, 'svg-container' ); }},'{mode}');"
	)
	element = await page.querySelector("div")
	svg = await page.evaluate("(element) => element.innerHTML", element)

	await browser.close()
	return svg


def trace(filename: str, blackAndWhite: bool = False, mode: str = "default") -> str:
	"""Do a trace of an image on the filesystem using the pyppeteer library.

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
	try:
		return asyncio.get_event_loop().run_until_complete(
			doTrace(filename.replace("\\", "/"), mode)
		)
	except ConnectionResetError:
		print("WARNING: ConnectionResetError - probably just a hiccup retrying")
		return asyncio.get_event_loop().run_until_complete(
			doTrace(filename.replace("\\", "/"), mode)
		)
