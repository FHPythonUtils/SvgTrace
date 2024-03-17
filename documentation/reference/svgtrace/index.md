# Svgtrace

[Svgtrace Index](../README.md#svgtrace-index) / Svgtrace

> Auto-generated documentation for [svgtrace](../../../svgtrace/__init__.py) module.

- [Svgtrace](#svgtrace)
  - [asyncTrace](#asynctrace)
  - [skimageTrace](#skimagetrace)
  - [trace](#trace)

## asyncTrace

[Show source in __init__.py:46](../../../svgtrace/__init__.py#L46)

Do a trace of an image on the filesystem using the playwright library.

#### Arguments

----
 - `filename` *str* - The location of the file on the filesystem, use an
 absolute filepath for this
 - `blackAndWhite` *bool, optional* - Trace a black and white SVG. Defaults to False.
 - `mode` *str, optional* - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
 for more information. Defaults to "default".

#### Returns

-------
 - `str` - SVG string

#### Raises

------
 FileNotFoundError f"{filename} does not exist!"
 OSError "svgtrace.trace/ asyncTrace is not supported in Windows Jupyter Notebooks"

#### Signature

```python
async def asyncTrace(
    filename: str, blackAndWhite: bool = False, mode: str = "default"
) -> str: ...
```



## skimageTrace

[Show source in __init__.py:111](../../../svgtrace/__init__.py#L111)

Do a trace of an pillow image using the skimage library.

#### Arguments

----
 - `image` *Image.Image* - pillow image to trace

#### Returns

-------
 - `str` - SVG string

#### Signature

```python
def skimageTrace(image: Image.Image) -> str: ...
```



## trace

[Show source in __init__.py:23](../../../svgtrace/__init__.py#L23)

Do a trace of an image on the filesystem using the playwright library.

#### Arguments

----
 - `filename` *str* - The location of the file on the filesystem, use an
 absolute filepath for this
 - `blackAndWhite` *bool, optional* - Trace a black and white SVG. Defaults to False.
 - `mode` *str, optional* - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
 for more information. Defaults to "default".

#### Returns

-------
 - `str` - SVG string

#### Raises

------
 FileNotFoundError f"{filename} does not exist!"

#### Signature

```python
def trace(filename: str, blackAndWhite: bool = False, mode: str = "default") -> str: ...
```