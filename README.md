[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/SvgTrace.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/2a0d815f69e543ecbe38b0720b4d359b.svg?style=for-the-badge)](https://www.codacy.com/manual/FHPythonUtils/SvgTrace)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/SvgTrace.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/SvgTrace.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/SvgTrace.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/SvgTrace.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/SvgTrace.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/svgtrace.svg?style=for-the-badge)](https://pypi.org/project/svgtrace/)
[![PyPI Version](https://img.shields.io/pypi/v/svgtrace.svg?style=for-the-badge)](https://pypi.org/project/svgtrace/)

<!-- omit in TOC -->
# SvgTrace

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Leverage pyppeteer and the imagetrace.js library to trace a bitmap to SVG in
python

## Example

Convert the following files:
<div>
<img src="logo-bw.png" alt="Screenshot 1" width="300">
<img src="logo.png" alt="Screenshot 2" width="300">
</div>


```python
""" Test the image tracer """

from pathlib import Path
from svgtrace import trace

THISDIR = str(Path(__file__).resolve().parent)

bw = open(THISDIR + "/logo-bw.svg", "w")
bw.write(trace(THISDIR + "/logo-bw.png", True))
bw.close()
colour = open(THISDIR + "/logo.svg", "w")
colour.write(trace(THISDIR + "/logo.png"))
colour.close()
```

Output

<div>
<img src="logo-bw.svg" alt="Screenshot 1" width="300">
<img src="logo.svg" alt="Screenshot 2" width="300">
</div>


## Install With PIP

```python
pip install svgtrace
```

Head to https://pypi.org/project/svgtrace/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```

## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/SvgTrace
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.
