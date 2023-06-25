<!-- omit in toc -->
# Tutorial

See below for a step-by-step tutorial on how to use svgtrace

- [Using the `trace` function](#using-the-trace-function)
- [Using the `asyncTrace` function](#using-the-asynctrace-function)
- [Using the `skimageTrace` function](#using-the-skimagetrace-function)

## Using the `trace` function

1. Create the following files (`logo-bw.png` and `logo.png`)
	<div>
	<img src="../../tests/data/logo-bw.png" alt="Screenshot 1" width="300">
	<img src="../../tests/data/logo.png" alt="Screenshot 2" width="300">
	</div>

2. Import `svgtrace` and convert a file on disk (with `trace`) to an svg, andsave this back to disk
   (with `Path().write_text`)
	```python
	from pathlib import Path
	from svgtrace import trace

	Path("logo-bw.svg").write_text(trace("logo-bw.png", True), encoding="utf-8")
	Path("logo.svg").write_text(trace("logo.png"), encoding="utf-8")
	```

3. Output
	<div>
	<img src="../../tests/data/logo-bw.svg" alt="logo-wb.svg" width="300">
	<img src="../../tests/data/logo.svg" alt="logo.svg" width="300">
	</div>

## Using the `asyncTrace` function

1. Import `svgtrace` and convert a file on disk (with `asyncTrace`) to an svg, andsave this back to disk
   (with `Path().write_text`)
	```python
	from pathlib import Path
	from svgtrace import trace

	Path("logo-asyncBw.svg").write_text(asyncio.run(asyncTrace("logo-bw.png", True)), encoding="utf-8")
	Path("logo-async.svg").write_text(asyncio.run(asyncTrace("logo.png")), encoding="utf-8")
	```

2. Output is identical to above

## Using the `skimageTrace` function

1. Import `svgtrace` and convert a pillow image (with `skimageTrace`) to an svg, andsave this back to disk
   (with `Path().write_text`)
	```python
	from pathlib import Path
	from PIL import Image
	from svgtrace import trace

	Path("logo-skimageBw.svg").write_text(skimageTrace(Image.open("logo-bw.png")), encoding="utf-8")
	Path("logo-skimage.svg").write_text(skimageTrace(Image.open("logo.png")), encoding="utf-8")
	```

2. Output
	<div>
	<img src="../../tests/data/logo-skimageBw.svg" alt="logo-skimageBw.svg" width="300">
	<img src="../../tests/data/logo-skimage.svg" alt="logo-skimage.svg" width="300">
	</div>
