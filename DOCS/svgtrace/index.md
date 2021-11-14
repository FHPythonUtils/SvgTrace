# svgtrace

> Auto-generated documentation for [svgtrace](../../svgtrace/__init__.py) module.

Author FredHappyface 2020.

- [Svgtrace](../README.md#svgtrace-index) / [Modules](../README.md#svgtrace-modules) / svgtrace
    - [doTrace](#dotrace)
    - [trace](#trace)

Uses pyppeteer to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below

## doTrace

[[find in source code]](../../svgtrace/__init__.py#L17)

```python
async def doTrace(filename: str, mode: str = 'default'):
```

Call web code.

## trace

[[find in source code]](../../svgtrace/__init__.py#L41)

```python
def trace(
    filename: str,
    blackAndWhite: bool = False,
    mode: str = 'default',
) -> str:
```

Do a trace of an image on the filesystem using the pyppeteer library.

#### Arguments

- `filename` *str* - The location of the file on the filesystem, use an
absolute filepath for this
- `blackAndWhite` *bool, optional* - Trace a black and white SVG. Defaults to False.
- `mode` *str, optional* - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
for more information. Defaults to "default".

#### Returns

- `str` - SVG string
