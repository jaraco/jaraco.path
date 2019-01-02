.. image:: https://img.shields.io/pypi/v/jaraco.path.svg
   :target: https://pypi.org/project/jaraco.path

.. image:: https://img.shields.io/pypi/pyversions/jaraco.path.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.path/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.path

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/skeleton/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/skeleton/branch/master

.. image:: https://img.shields.io/travis/jaraco/jaraco.path/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.path

Hidden File Detection
---------------------

``jaraco.path`` provides cross platform hidden file detection::

    from jaraco import path
    if path.is_hidden('/'):
        print("Your root is hidden")

    hidden_dirs = filter(is_hidden, os.listdir('.'))
