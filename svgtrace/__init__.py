"""Author FredHappyface 2020.

Uses playwright to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below
"""

from __future__ import annotations

import asyncio
import sys
import warnings
from pathlib import Path

import numpy as np
from install_playwright import install
from PIL import Image
from playwright.async_api import async_playwright
from skimage import feature, measure

THISDIR = str(Path(__file__).resolve().parent)


def trace(filename: str, blackAndWhite: bool = False, mode: str = "default") -> str:
	"""Do a trace of an image on the filesystem using the playwright library.

	Args:
	----
		filename (str): The location of the file on the filesystem, use an
		absolute filepath for this
		blackAndWhite (bool, optional): Trace a black and white SVG. Defaults to False.
		mode (str, optional): Set the mode. See https://github.com/jankovicsandras/imagetracerjs
		for more information. Defaults to "default".

	Returns:
	-------
		str: SVG string

	Raises:
	------
		FileNotFoundError f"{filename} does not exist!"

	"""
	return asyncio.run(asyncTrace(filename, blackAndWhite, mode))


async def asyncTrace(filename: str, blackAndWhite: bool = False, mode: str = "default") -> str:
	"""Do a trace of an image on the filesystem using the playwright library.

	Args:
	----
		filename (str): The location of the file on the filesystem, use an
		absolute filepath for this
		blackAndWhite (bool, optional): Trace a black and white SVG. Defaults to False.
		mode (str, optional): Set the mode. See https://github.com/jankovicsandras/imagetracerjs
		for more information. Defaults to "default".

	Returns:
	-------
		str: SVG string

	Raises:
	------
		FileNotFoundError f"{filename} does not exist!"
		OSError "svgtrace.trace/ asyncTrace is not supported in Windows Jupyter Notebooks"

	"""
	# Detecting Default event loop in Notebook 6.1.6 on Windows is not ProactorEventLoop
	# (https://github.com/jupyter/notebook/issues/5916)
	if sys.platform.startswith("win") and sys.version_info >= (3, 8):
		try:
			from asyncio import WindowsSelectorEventLoopPolicy
		except ImportError:
			pass
		else:
			if isinstance(asyncio.get_event_loop_policy(), WindowsSelectorEventLoopPolicy):
				msg = "svgtrace.trace/ asyncTrace is not supported in Windows Jupyter Notebooks"
				raise OSError(
					msg
				)

	#
	if mode.find("black") >= 0 or blackAndWhite:
		mode = "posterized1"

	filename = filename.replace("\\", "/")

	if not Path(filename).exists():
		msg = f"{filename} does not exist!"
		raise FileNotFoundError(msg)

	async with async_playwright() as p:
		install(p.chromium)
		browser = await p.chromium.launch(
			args=[
				"--no-sandbox",
				"--disable-web-security",
				"--allow-file-access-from-files",
			]
		)

		page = await browser.new_page()
		await page.goto(f"file:///{THISDIR}/imagetracer.html")
		await page.evaluate(
			f"ImageTracer.imageToSVG('file:///{filename}',function(svgstr){{ ImageTracer.appendSVGString( svgstr, 'svg-container' ); }},'{mode}');"
		)
		element = await page.query_selector("div")
		svg = await page.evaluate("(element) => element.innerHTML", element)

		await browser.close()
	return svg


def skimageTrace(image: Image.Image) -> str:
	"""Do a trace of an pillow image using the skimage library.

	Args:
	----
		image (Image.Image): pillow image to trace

	Returns:
	-------
		str: SVG string

	"""
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore")
		imageGreyscale = image.convert("L")
	edges = feature.canny(np.array(imageGreyscale))
	paths = []
	contours = measure.find_contours(edges, 0.5)
	for contour in contours:
		pathData = " L ".join([f"{coord[1]},{coord[0]}" for coord in contour])
		paths.append(f'<path d="M {pathData} Z" stroke="black" fill="none" />')

	return (
		f'<svg xmlns="http://www.w3.org/2000/svg" width="{image.width}" height="{image.height}">'
		+ "".join(paths)
		+ "</svg>"
	)
