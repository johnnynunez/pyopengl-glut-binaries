# PyOpenGL-glut-binaries

Prebuilt Windows freeglut and GLE libraries for [PyOpenGL](
https://github.com/mcfletch/pyopengl).

`OpenGL.GLUT` and `OpenGL.GLE` wrap two C libraries that Windows does not
ship. This distribution carries builds of both, so a Windows user gets them
by asking:

```
pip install PyOpenGL[glut]
```

Nothing to call and nothing to configure: PyOpenGL finds the directory itself.
A freeglut the *system* provides still wins over these, because a user who
installed their own meant it.

## Why it is a package of its own

The same builds shipped inside PyOpenGL itself, in every wheel on every
platform, so a Linux server rendering headlessly through EGL downloaded six
freeglut builds it could never load. As a separate, platform-tagged
distribution they reach the machines that can use them and no others, and a
scanner that objects to a decade-old vendored binary objects to a package only
GLUT users install rather than to PyOpenGL.

## What is here

Six builds of each library, because PyOpenGL asks for one exact name composed
from the running interpreter's word size and compiler generation:

| | 32-bit | 64-bit |
|---|---|---|
| **vc9** (Visual Studio 2008) | `freeglut32.vc9.dll`, `gle32.vc9.dll` | `freeglut64.vc9.dll`, `gle64.vc9.dll` |
| **vc10** (Visual Studio 2010) | `freeglut32.vc10.dll`, `gle32.vc10.dll` | `freeglut64.vc10.dll`, `gle64.vc10.dll` |
| **vc14** (Visual Studio 2015 and later) | `freeglut32.vc14.dll`, `gle32.vc14.dll` | `freeglut64.vc14.dll`, `gle64.vc14.dll` |

Both the `win32` and the `win_amd64` wheel carry all twelve, along with the
upstream licence and readme files. The word sizes are not split between the
two wheels: a split would halve the download and is a change to make on its
own, where a regression in it is attributable.

## Using it directly

PyOpenGL is the intended caller, but the path is public:

```python
from pyopengl_glut_binaries import DLL_DIRECTORY
```

`BUILDS` lists the base names above and `LIBRARIES` says where each library
came from.

## Licensing

The packaging is BSD-licensed; see `LICENSE`. The libraries are third-party
works under their own terms, which ship beside them in
`src/pyopengl_glut_binaries/DLLS/`:

- **freeglut** — 3.0.0-1.mp for MSVC, Martin Payne's build.
  [freeglut](http://freeglut.sourceforge.net/) upstream publishes source
  rather than Windows binaries. X-Consortium licence, in
  `freeglut_COPYING.txt`.
- **GLE** — the tubing and extrusion library, built as a Windows DLL. See
  `gle_COPYING`, `gle_COPYING.src` and `gle_AUTHORS`.

## Releases

A push to `main` runs the tests; if they are green and `__version__` in
`src/pyopengl_glut_binaries/__init__.py` is not already on PyPI, the wheels and
the sdist are built and published. Bumping the version is what cuts a release.

Issues go to [the PyOpenGL tracker](https://github.com/mcfletch/pyopengl/issues).
