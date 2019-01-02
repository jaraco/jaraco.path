import os
import platform
import ctypes

import six
import pytest

from jaraco import path


def test_is_hidden_not(tmpdir):
	"""
	A visible directory is not hidden.
	"""
	target = six.text_type(tmpdir)
	assert not path.is_hidden(target)


def test_is_hidden_not_abspath(tmpdir):
	"""
	A visible directory, even if referenced by a relative path,
	should not be considered hidden.
	"""
	target = six.text_type(tmpdir) + '/.'
	assert not path.is_hidden(target)


def test_is_hidden():
	assert path.is_hidden('.hg')


@pytest.mark.skipif(
	platform.system() != 'Windows',
	reason="Windows only")
def test_is_hidden_Windows(tmpdir):
	target = os.path.join(tmpdir, 'test')
	ctypes.SetFileAttributes(target, 2)
	assert path.is_hidden(target)
	assert path.is_hidden_Windows(target)


@pytest.mark.skipif(
	platform.system() != 'Darwin',
	reason="Darwin only")
def test_is_hidden_Darwin():
	# cheat because ~/Library is presumably hidden
	target = os.path.expanduser('~/Library')
	assert path.is_hidden(target)
	assert path.is_hidden_Darwin(target)
