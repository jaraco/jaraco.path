import os
import platform

import pytest

from jaraco import path


def test_is_hidden_not(tmpdir):
    """
    A visible directory is not hidden.
    """
    target = str(tmpdir)
    assert not path.is_hidden(target)


def test_is_hidden_not_abspath(tmpdir):
    """
    A visible directory, even if referenced by a relative path,
    should not be considered hidden.
    """
    target = str(tmpdir) + '/.'
    assert not path.is_hidden(target)


def test_is_hidden():
    assert path.is_hidden('.hg')


def test_is_hidden_Windows(tmpdir):
    SetFileAttributes = pytest.importorskip(
        'jaraco.windows.api.filesystem.SetFileAttributes'
    )
    target = os.path.join(tmpdir, 'test')
    SetFileAttributes(target, 2)
    assert path.is_hidden(target)
    assert path.is_hidden_Windows(target)


@pytest.mark.skipif(platform.system() != 'Darwin', reason="Darwin only")
def test_is_hidden_Darwin():
    # cheat because ~/Library is presumably hidden
    target = os.path.expanduser('~/Library')
    assert path.is_hidden(target)
    assert path.is_hidden_Darwin(target)
