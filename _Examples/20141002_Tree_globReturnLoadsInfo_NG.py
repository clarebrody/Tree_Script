#!/usr/bin/python

import os
import sys

file = '/Volumes/Camilla/DI/_Wrangling/temp_clare/Scripts/_Python_Scripts/_Tree_Scripting/FAB_VFX_PRP0064_20140925'

#returns [base name, padding, filetype, number of files, first file, last file]
def getSeqInfo(file):
	dir = os.path.dirname(file)
	file = os.path.basename(file)
	segNum = re.findall(r'\d+', file)[-1]
	numPad = len(segNum)
	baseName = file.split(segNum)[0]
	fileType = file.split('.')[-1]
	globString = baseName
	for i in range(0,numPad): globString += '?'
	theGlob = glob.glob(dir+'\\'+globString+file.split(segNum)[1])
	numFrames = len(theGlob)
	firstFrame = theGlob[0]
	lastFrame = theGlob[-1]
	return [baseName, numPad, fileType, numFrames, firstFrame, lastFrame]