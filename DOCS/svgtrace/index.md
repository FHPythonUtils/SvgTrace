# svgtrace

> Auto-generated documentation for [svgtrace](../../svgtrace/__init__.py) module.

Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below

- [Svgtrace](../README.md#svgtrace-index) / [Modules](../README.md#svgtrace-modules) / svgtrace
    - [doTrace](#dotrace)
    - [trace](#trace)

## doTrace

[[find in source code]](../../svgtrace/__init__.py#L14)

```python
async def doTrace(filename: str, mode: str = 'default'):
```

Main method to call web code

## trace

[[find in source code]](../../svgtrace/__init__.py#L30)

```python
def trace(
    filename: str,
    blackAndWhite: bool = False,
    mode: str = 'default',
) -> str:
```

Do a trace of an image on the filesystem using the pyppeteer library

#### Arguments

- `filename` *str* - The location of the file on the filesystem, use an
absolute filepath for this
- `blackAndWhite` *bool, optional* - Trace a black and white SVG. Defaults to False.
- `mode` *str, optional* - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
for more information. Defaults to "default".

#### Returns

- `str` - SVG string
