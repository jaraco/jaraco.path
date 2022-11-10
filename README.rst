.. image:: https://img.shields.io/pypi/v/jaraco.path.svg
   :target: https://pypi.org/project/jaraco.path

.. image:: https://img.shields.io/pypi/pyversions/jaraco.path.svg

.. image:: https://github.com/jaraco/jaraco.path/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.path/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2022-informational
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
