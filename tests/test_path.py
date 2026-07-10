import os
import pathlib
import platform

import pytest
from _pytest._py.path import LocalPath

from jaraco import path


def test_is_hidden_not(tmpdir: LocalPath) -> None:
    """
    A visible directory is not hidden.
    """
    target = str(tmpdir)
    assert not path.is_hidden(target)


def test_is_hidden_not_abspath(tmpdir: LocalPath) -> None:
    """
    A visible directory, even if referenced by a relative path,
    should not be considered hidden.
    """
    target = str(tmpdir) + '/.'
    assert not path.is_hidden(target)


def test_is_hidden() -> None:
    assert path.is_hidden('.hg')


def test_is_hidden_Windows(tmpdir: LocalPath) -> None:
    SetFileAttributes = pytest.importorskip(
        'jaraco.windows.api.filesystem.SetFileAttributes'
    )
    target = os.path.join(tmpdir, 'test')
    SetFileAttributes(target, 2)
    assert path.is_hidden(target)
    assert path.is_hidden_Windows(target)


@pytest.mark.skipif(platform.system() != 'Darwin', reason="Darwin only")
def test_is_hidden_Darwin() -> None:
    # cheat because ~/Library is presumably hidden
    target = os.path.expanduser('~/Library')
    assert path.is_hidden(target)
    assert path.is_hidden_Darwin(target)


def test_TreeMaker_Protocol() -> None:
    # Ensure the validity of the TreeMaker Protocol both statically and at runtime
    tree_maker: path.TreeMaker
    tree_maker = pathlib.Path()
    assert isinstance(tree_maker, path.TreeMaker)
    tree_maker = path.Recording()
    assert isinstance(tree_maker, path.TreeMaker)
