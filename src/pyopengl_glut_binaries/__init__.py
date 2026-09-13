"""Prebuilt Windows freeglut and GLE libraries for PyOpenGL.

``OpenGL.GLUT`` and ``OpenGL.GLE`` wrap two C libraries that Windows does not
ship. This package carries builds of them, so that
``pip install PyOpenGL[glut]`` is all a Windows user needs for either.

The only thing a caller wants from this module is where the files are:

    >>> import os
    >>> from pyopengl_glut_binaries import DLL_DIRECTORY
    >>> os.path.isdir(DLL_DIRECTORY)
    True

PyOpenGL reads that itself, in ``OpenGL.platform.ctypesloader``, and a library
the *system* provides still wins over these -- a user who installed their own
freeglut meant it. So nothing here needs calling; installing the package is the
whole of the interface.

Which file answers is PyOpenGL's decision: it asks for one exact name built
from the running interpreter's word size and the compiler generation, which is
why there are six builds of each library rather than one. See
:data:`BUILDS` for what is here.
"""

import os

__version__ = '1.0.0'

__all__ = ['BUILDS', 'DLL_DIRECTORY', 'LIBRARIES', '__version__']

#: Where the libraries are, as an absolute path.
#:
#: A directory rather than a list of files, because the caller composes a name
#: from its own word size and looks for that one.
DLL_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DLLS')

#: The libraries carried here, and where each came from.
LIBRARIES = {
    'freeglut': (
        "freeglut 3.0.0-1.mp for MSVC -- Martin Payne's build, since freeglut "
        'upstream publishes source rather than Windows binaries. Not the '
        'original GLUT: these export glutMainLoopEvent and the rest of '
        "freeglut's additions."
    ),
    'gle': 'the GLE tubing and extrusion library, built as a Windows DLL',
}

#: The word sizes and compiler generations each library is built for.
#:
#: ``vc9`` is Visual Studio 2008, ``vc10`` is 2010 and ``vc14`` is 2015 and
#: later. PyOpenGL asks for the generation matching the interpreter that is
#: running, so all six of each are here rather than only the newest.
BUILDS = tuple(
    '%s%s.%s' % (library, size, vc)
    for library in ('freeglut', 'gle')
    for size in ('32', '64')
    for vc in ('vc9', 'vc10', 'vc14')
)
