.. image:: https://img.shields.io/pypi/v/jaraco.path.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.path.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.path

.. image:: https://github.com/jaraco/jaraco.path/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.path/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest


Hidden File Detection
---------------------

``jaraco.path`` provides cross platform hidden file detection::

    from jaraco import path
    if path.is_hidden('/'):
        print("Your root is hidden")

    hidden_dirs = filter(is_hidden, os.listdir('.'))
