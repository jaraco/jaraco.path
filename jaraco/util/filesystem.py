#!/usr/bin/env python

import os
import re

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

	def __div__(self, child):
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