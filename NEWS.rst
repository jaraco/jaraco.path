v3.7.2
======

Bugfixes
--------

- Fix ``FilesSpec`` parameters variance issues by making it a `typing.Mapping` instead of a `dict` -- by :user:`Avasam` (#3)


v3.7.1
======

No significant changes.


v3.7.0
======

Features
--------

- Require Python 3.8 or later.


v3.6.0
======

Added support for ``Symlink``s for the tree maker (``build``).

v3.5.0
======

Introduced ``Recording`` object and ``TreeMaker`` protocol,
with ``build()`` now explicitly accepting any ``TreeMaker``.

v3.4.1
======

Fixed EncodingWarnings and ResourceWarnings.

v3.4.0
======

Require Python 3.7 or later.

v3.3.1
======

Once again attempt to disable PyPy dependency.

v3.3.0
======

Disabled PyObjC dependency on PyPy where it's unsupported.

Switched to native namespace package.

v3.2.0
======

Added ``jaraco.path.build`` for building dir trees from a
Python dictionary spec.

v3.1.0
======

Properly declared dependency on pyobjc for macOS.

v3.0.0
======

Require Python 3.6 or later.

2.0
===

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

1.2
===

Move to Github and configure automatic releases via Travis-CI.

1.1
===

Add cross platform is_hidden function.

1.0
===

Initial released based on jaraco.util 10.13.
