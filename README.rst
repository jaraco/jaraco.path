.. image:: https://img.shields.io/pypi/v/jaraco.path.svg
   :target: https://pypi.org/project/jaraco.path

.. image:: https://img.shields.io/pypi/pyversions/jaraco.path.svg

.. image:: https://img.shields.io/pypi/dm/jaraco.path.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.path/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.path

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Hidden File Detection
---------------------

``jaraco.path`` provides cross platform hidden file detection::

    from jaraco import path
    if path.is_hidden('/'):
        print("Your root is hidden")

    hidden_dirs = filter(is_hidden, os.listdir('.'))
