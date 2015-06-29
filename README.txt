jaraco.path
===========

Hidden File Detection
---------------------

``jaraco.path`` provides cross platform hidden file detection::

    from jaraco import path
    if path.is_hidden('/'):
        print("Your root is hidden")

    hidden_dirs = filter(is_hidden, os.listdir('.'))
