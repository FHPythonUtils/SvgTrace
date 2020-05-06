<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

<a name=".svgtrace"></a>
## svgtrace

Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below

<a name=".svgtrace.doTrace"></a>
#### doTrace

```python
async doTrace(filename, mode="default")
```

Main method to call web code

<a name=".svgtrace.trace"></a>
#### trace

```python
trace(filename, blackAndWhite=False, mode="default")
```

Do a trace of an image on the filesystem using the pyppeteer library

**Arguments**:

- `filename` _string_ - The location of the file on the filesystem, use an
  absolute filepath for this
- `blackAndWhite` _bool, optional_ - Trace a black and white SVG. Defaults to False.
- `mode` _str, optional_ - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
  for more information. Defaults to "default".
  

**Returns**:

- `str` - SVG string

