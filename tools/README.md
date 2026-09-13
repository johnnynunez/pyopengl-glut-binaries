# Where the binaries came from

What produced the files in `src/pyopengl_glut_binaries/DLLS/`, kept so that the
provenance of a vendored binary is answerable. It travelled here from
PyOpenGL's `src/` when the binaries did.

| | what it is |
|---|---|
| `buildgledll.py` | Fetches GLE 3.1.0 source and builds it with MSVC, once per word size and compiler generation. |
| `gle32.zip` | A prebuilt `gle32.dll` with its `AUTHORS`, `COPYING` and `GLE_WIN32_README.txt` — the three GLE files that ship beside the binaries came from here. |

`buildgledll.py` does not run on a current machine: it wants a Visual Studio
2008 command prompt. It is preserved as it was rather than modernised, because
nothing here can run it and so nothing here could tell whether a change broke
it. `[tool.ruff]` in `pyproject.toml` excludes this directory for the same
reason.

It builds under the name `opengle` rather than `gle`: the note in its docstring
records why, which is that a DMCA notice against the name `gle.dll` once took
PyOpenGL offline.

## There is no recipe for the freeglut builds

Every `freeglut*.dll` here is **freeglut**, not Mark Kilgard's original GLUT:
each exports `glutMainLoopEvent`, `glutLeaveMainLoop` and
`glutInitContextVersion`, which classic GLUT has none of. They are freeglut
**3.0.0-1.mp for MSVC**, Martin Payne's build, as
`src/pyopengl_glut_binaries/DLLS/freeglut_README.txt` records — freeglut
upstream publishes source rather than Windows binaries.

They came from that third party's download rather than from anything in this
directory, so unlike GLE there is nothing here to rebuild them with. Anyone
doing that starts by choosing where the new binaries come from.

Rebuilding any of this is a decision on its own, separate from the packaging
split that moved these files here — see `BUNDLED-DLLS.md` in PyOpenGL's
`plans/`.
