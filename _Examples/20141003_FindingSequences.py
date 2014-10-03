#!/usr/bin/python

import fnmatch
import os
from os import listdir, sep
from os.path import abspath, basename, isdir
from sys import argv
 
#dirPath = '/Volumes/Camilla/DI/_Wrangling/temp_clare/Scripts/_Python_Scripts/_Tree_Scripting/FAB_VFX_PRP0064_20140925'
#pattern = '*.dpx'

#first attempt at finding min and max numbers, 
#stops if it finds dpx and doesn't go on to the next directory
#
for root, dir, files in os.walk("/Users/clarebrody/Documents/Personal/Work/Scripts/TES_SEQ_PRP0001_20141001"):
#        	print root
        	for curDir in dir:
        		fulldir = os.path.join(root, curDir)
        	print ""
	       	for items in sorted(fnmatch.filter(files, "*")):
	       		if not items.startswith('.') and os.path.isfile(os.path.join(root, items)):
	       			print "min value element : ",root, min(sorted(fnmatch.filter(files, "*")))
	       			print "max value element : ",root, max(sorted(fnmatch.filter(files, "*")))
			break
##	       		minframeSeq = min (list(items))
##	       		print "..." + items
##			print minframeSeq
##        	print ""
##        	print min(sorted(fnmatch.filter(files, "*")))
##        	result = {}
##        	sortedList = []

#second attempt at finding all the dpx
#
#searchdir = r'/Users/clarebrody/Documents/Personal/Work/Scripts/TES_SEQ_PRP0001_20141001'  # your search starts in this directory (your root) 
#
#count = 0
#for root, dirs, files in os.walk(searchdir):
#    for name in files:
#        (base, ext) = os.path.splitext(name) # split base and extension
#        if ext in ('.jpg', '.gif', '.dpx'):          # check the extension
#            count += 1
#            full_name = os.path.join(root, name) # create full path
#            print (full_name).sort
#        
##print('\ntotal number of .jpg and .gif files found: %d' % count)
##print min(full_name), max(full_name)
#