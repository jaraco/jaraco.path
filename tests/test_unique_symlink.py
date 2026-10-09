import os

import pytest

from jaraco.path import get_unique_pathname


def test_unique_pathname_skips_dangling_links(tmp_path):
    original = tmp_path / 'output.txt'
    numbered = tmp_path / 'output (1).txt'
    for path in (original, numbered):
        try:
            path.symlink_to(tmp_path / 'missing-target')
        except OSError as exc:
            pytest.skip(f'Symlinks are unavailable: {exc}')

    candidate = get_unique_pathname('output.txt', root=str(tmp_path))
    assert candidate == str(tmp_path / 'output (2).txt')
    assert not os.path.lexists(candidate)
    assert original.is_symlink()
    assert numbered.is_symlink()


def test_unique_pathname_returns_unused_path(tmp_path):
    assert get_unique_pathname('new.txt', root=str(tmp_path)) == str(
        tmp_path / 'new.txt'
    )
