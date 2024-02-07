.. image:: https://img.shields.io/pypi/v/jaraco.path.svg
   :target: https://pypi.org/project/jaraco.path

.. image:: https://img.shields.io/pypi/pyversions/jaraco.path.svg

.. image:: https://github.com/jaraco/jaraco.path/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.path/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2024-informational
   :target: https://blog.jaraco.com/skeleton

Hidden File Detection
---------------------

``jaraco.path`` provides cross platform hidden file detection::

    from jaraco import path
    if path.is_hidden('/'):
        print("Your root is hidden")

    hidden_dirs = filter(is_hidden, os.listdir('.'))


Directory Builder
-----------------

When testing (and perhaps in other cases), it's often necessary to construct
a tree of directories/files. This project provides a ``build`` function to
simply create such a directory from a dictionary definition::

    from jaraco.path import build
    build(
        {
            'foo': 'Content of foo',
            'subdir': {
                'foo': 'Content of subdir/foo',
            },
        },
    )
