# Svgtrace

[Svgtrace Index](../README.md#svgtrace-index) /
Svgtrace

> Auto-generated documentation for [svgtrace](../../../svgtrace/__init__.py) module.

- [Svgtrace](#svgtrace)
  - [trace](#trace)

## trace

[Show source in __init__.py:17](../../../svgtrace/__init__.py#L17)

Do a trace of an image on the filesystem using the playwright library.

#### Arguments

- `filename` *str* - The location of the file on the filesystem, use an
absolute filepath for this
- `blackAndWhite` *bool, optional* - Trace a black and white SVG. Defaults to False.
- `mode` *str, optional* - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
for more information. Defaults to "default".

#### Returns

- `str` - SVG string

#### Raises

FileNotFoundError f"{filename} does not exist!"

#### Signature

```python
def trace(filename: str, blackAndWhite: bool = False, mode: str = "default") -> str:
    ...
```


