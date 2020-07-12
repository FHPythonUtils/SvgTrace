Module svgtrace
===============
Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below

Functions
---------

    
`doTrace(filename, mode='default')`
:   Main method to call web code

    
`trace(filename, blackAndWhite=False, mode='default')`
:   Do a trace of an image on the filesystem using the pyppeteer library
    
    Args:
            filename (string): The location of the file on the filesystem, use an
            absolute filepath for this
            blackAndWhite (bool, optional): Trace a black and white SVG. Defaults to False.
            mode (str, optional): Set the mode. See https://github.com/jankovicsandras/imagetracerjs
            for more information. Defaults to "default".
    
    Returns:
            str: SVG string