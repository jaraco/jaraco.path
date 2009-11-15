# -*- coding: UTF-8 -*-

"""jaraco.filesystem:
	tools for working with files and file systems
	
Copyright © 2004 Jason R. Coombs  
"""

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'
__version__ = '$Rev$'[6:-2]
__svnauthor__ = '$Author$'[9:-2]
__date__ = '$Date$'[7:-2]

import os
import itertools
import calendar
import logging

log = logging.getLogger(__name__)

def GetUniquePathname(path, root = ''):
	"""Return a pathname possibly with a number appended to it so that it is
	unique in the directory."""
	path = os.path.join(root, path)
	# consider the path supplied, then the paths with numbers appended
	potentialPaths = itertools.chain((path,), __GetNumberedPaths__(path))
	potentialPaths = itertools.ifilterfalse(os.path.exists, potentialPaths)
	return potentialPaths.next()

GetUniqueFilename = GetUniquePathname

def __GetNumberedPaths__(filepath):
	"""Append numbers in sequential order to the filename or folder name
	Numbers should be appended before the extension on a filename."""
	format = '%s (%%d)%s' % __splitext__(filepath)
	return itertools.imap(lambda n: format % n, itertools.count(1))

def __splitext__(filepath):
	"Custom version of splitext that doesn't perform splitext on directories"
	if os.path.isdir(filepath):
		return filepath, ''
	else:
		return os.path.splitext(filepath)

def set_time(filename, mod_time):
	"""
	Set the modified time of a file
	"""
	log.debug('Setting modified time to %s', mod_time)
	mtime = calendar.timegm(mod_time.utctimetuple())
	atime = os.stat(filename).st_atime
	os.utime(filename, (atime, mtime))
