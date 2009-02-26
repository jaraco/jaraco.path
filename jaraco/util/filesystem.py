#!/usr/bin/env python

class RelativePath(str):
	"""
	An object that abstracts and simplifies path handling.  Just
	create one and either call a child path and you should get a
	suitable path.
	
	>>> p = RelativePath(r'c:\Windows')
	>>> p('System32') == r'c:\Windows\System32'
	True
	"""
	def __new__(self, value):
		return str.__new__(self, value)

	def __call__(self, *children):
		return RelativePath(os.path.join(self, *children))
	
	# can't override the __add__ because os.path.join uses it
	#  to append a backslash.
	#def __add__(self, child):
	#	return self(child)

