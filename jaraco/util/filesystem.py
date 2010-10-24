#!/usr/bin/env python
from __future__ import division, absolute_import

import os
import re
import tempfile
import functools

class RelativePath(str):
	"""
	An object that abstracts and simplifies path handling.  Just
	create one and either call a child path and you should get a
	suitable path.
	
	>>> p = RelativePath(r'c:\Windows')
	>>> p('System32') == os.path.join(r'c:\Windows', 'System32')
	True
	"""
	def __call__(self, *children):
		return RelativePath(os.path.join(self, *children))
	
	# can't override the __add__ because os.path.join uses it
	#  to append a backslash.
	#def __add__(self, child):
	#	return self(child)

	def __truediv__(self, child):
		"""
		Override / for getting a child path
		>>> RelativePath("/usr") / 'bin' == os.path.join('/usr', 'bin')
		True
		"""
		return self(child)

def encode(name, system='NTFS'):
	"""
	Encode the name for a suitable name in the given filesystem
	>>> encode('Test :1')
	'Test _1'
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

def replace_extension(new_ext, filename):
	"""
	>>> replace_extension('.pdf', 'myfile.doc')
	'myfile.pdf'
	"""
	return os.path.splitext(filename)[0] + new_ext

def ExtensionReplacer(new_ext):
	"""
	A reusable function to replace a file's extension with another
	
	>>> repl = ExtensionReplacer('.pdf')
	>>> repl('myfile.doc')
	'myfile.pdf'
	>>> repl('myfile.txt')
	'myfile.pdf'
	>>> repl('myfile')
	'myfile.pdf'
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
