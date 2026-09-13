#! /usr/bin/env python3
"""A wheel that is platform-specific without holding an extension module.

The payload is prebuilt Windows DLLs, so the wheel this project produces has
to carry a platform tag: the whole reason the binaries live in a distribution
of their own is that a Linux or macOS install never downloads them, and only
the tag achieves that. setuptools decides purity from whether there are
extension modules to build, and there are none here -- the DLLs are data --
so it would produce ``py3-none-any`` and every platform would get them again.

There is nothing to compile, so the tag is the only thing this file exists for;
everything else about the project is declared in ``pyproject.toml``.
"""

from setuptools import setup
from setuptools.command.bdist_wheel import bdist_wheel as _bdist_wheel
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    """A distribution whose contents are platform-specific.

    ``has_ext_modules`` is what ``bdist_wheel`` asks, and answering yes is what
    makes the wheel's root impure and so gives it a platform tag.
    """

    def has_ext_modules(self):
        return True


class bdist_wheel(_bdist_wheel):
    """Tag the wheel for the platform but for no particular interpreter.

    The default tag for an impure wheel names the interpreter and ABI that
    built it -- ``cp313-cp313-win_amd64`` -- because that is what a compiled
    extension is tied to. A DLL loaded through ctypes is tied to neither, so
    the tag is ``py3-none-<platform>``: one wheel per platform serves every
    Python 3 rather than one per interpreter release.

    ``--plat-name`` still chooses the platform, which is how a single Windows
    runner produces both the ``win32`` and the ``win_amd64`` wheel.
    """

    def get_tag(self):
        _python, _abi, platform = super().get_tag()
        return 'py3', 'none', platform


setup(distclass=BinaryDistribution, cmdclass={'bdist_wheel': bdist_wheel})
