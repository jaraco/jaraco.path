#!/usr/bin/env python
from __future__ import division, absolute_import, unicode_literals

import os
import re
import tempfile
import functools
import contextlib

def encode(name, system='NTFS'):
	"""
	Encode the name for a suitable name in the given filesystem
	>>> encode('Test :1')
	u'Test _1'
	"""
	assert system == 'NTFS', 'unsupported filesystem'
	special_characters = r'<>:"/\|?*' + ''.join(map(chr, range(32)))
	pattern = '|'.join(map(re.escape, special_characters))
	pattern = re.compile(pattern)
	return pattern.sub('_', name)

class save_to_file():
	"""
	A context manager for saving some content to a file, and then
	cleaning up the file afterward.

	>>> with save_to_file('foo') as filename: assert 'foo' == open(filename).read()
	"""
	def __init__(self, content):
		self.content = content

	def __enter__(self):
		fd, self.filename = tempfile.mkstemp()
		file = os.fdopen(fd, 'wb')
		file.write(self.content)
		file.close()
		return self.filename

	def __exit__(self, type, value, traceback):
		os.remove(self.filename)

@contextlib.contextmanager
def tempfile_context(*args, **kwargs):
	"""
	A wrapper around tempfile.mkstemp to create the file in a context and
	delete it after.
	"""
	fd, filename = tempfile.mkstemp(*args, **kwargs)
	os.close(fd)
	try:
		yield filename
	finally:
		os.remove(filename)

def replace_extension(new_ext, filename):
	"""
	>>> replace_extension('.pdf', 'myfile.doc')
	u'myfile.pdf'
	"""
	return os.path.splitext(filename)[0] + new_ext

def ExtensionReplacer(new_ext):
	"""
	A reusable function to replace a file's extension with another

	>>> repl = ExtensionReplacer('.pdf')
	>>> repl('myfile.doc')
	u'myfile.pdf'
	>>> repl('myfile.txt')
	u'myfile.pdf'
	>>> repl('myfile')
	u'myfile.pdf'
	"""
	return functools.partial(replace_extension, new_ext)

def ensure_dir_exists(func):
	"wrap a function that returns a dir, making sure it exists"
	@functools.wraps(func)
	def make_if_not_present():
		dir = func()
		if not os.path.isdir(dir):
			os.makedirs(dir)
		return dir
	return make_if_not_present

def read_chunks(file, chunk_size=2048, update_func=lambda x: None):
	"""
	Read file in chunks of size chunk_size (or smaller).
	If update_func is specified, call it on every chunk with the amount
	read.
	"""
	while(True):
		res = file.read(chunk_size)
		if not res: break
		update_func(len(res))
		yield res
