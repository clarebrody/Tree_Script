#!/usr/bin/python

import os, sys
#from sets import Set
path = '/Volumes/Camilla/DI/_Wrangling/temp_clare/Scripts/_Python_Scripts/_Tree_Scripting/FAB_VFX_PRP0064_20140925'
files = os.listdir(path)

finalSeqList = []

def padFrame(frame,pad):
    return '0' * (pad - len(str(frame))) + str(frame)

def seqLS (dirPath):
    files = os.listdir(dirPath)
    for file in files:
        try:
            prefix, frame, suffix = file.split('.')
    
            # build a dictionary of the sequences as {name: frames, suffix}
            #
            # eg beauty.01.tif ... beauty.99.tif  will convert to
            # { beauty : [01,02,...,98,99], tif }
    
            try:
                result[prefix][0].append(frame)
            except KeyError:
                # we have a new file sequence, so create a new key:value pair
                result[prefix] = [[frame],suffix]   
        except ValueError:
            # the file isn't in a sequence, add a dummy key:value pair
            result[file] = file
    
    
    for prefix in result:
        if result[prefix] != prefix:
            frames = result[prefix][0]
            frames.sort()
    
            # find gaps in sequence
            startFrame = int(frames[0])
            endFrame = int(frames[-1])
            pad = len(frames[0])
            idealRange = set(range(startFrame,endFrame))
            realFrames = set([int(x) for x in frames])
            # sets can't be sorted, so cast to a list here
            missingFrames = list(idealRange - realFrames)
            missingFrames.sort()
    
            #calculate fancy ranges
            subRanges = []
            for gap in missingFrames:
                if startFrame != gap:
                    rangeStart = padFrame(startFrame,pad)
                    rangeEnd  = padFrame(gap-1,pad)
                    subRanges.append('-'.join([rangeStart, rangeEnd]))
                startFrame = gap+1
                
            subRanges.append('-'.join([padFrame(startFrame,pad), padFrame(endFrame,pad) ]))
            frameRanges = ','.join(subRanges)
            frameRanges = '[%s]' % (frameRanges)
            suffix = result[prefix][1]
            sortedList.append('.'.join([prefix, frameRanges ,suffix]))
            print ('\t' + '.'.join([prefix, frameRanges ,suffix]))
        else: sortedList.append(prefix)
   
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        
    for root, dirs, files in os.walk(path):
        for curDir in dirs:
            fulldir = os.path.join(root, curDir)
            print 'Scanning : %s' % (fulldir)
            result = {}
            sortedList = []
            seqLS(fulldir)

#returns [base name, padding, filetype, number of files, first file, last file]
#def getSeqInfo(file):
#	dir = os.path.dirname(file)
#	file = os.path.basename(file)
#	segNum = re.findall(r'\d+', file)[-1]
#	numPad = len(segNum)
#	baseName = file.split(segNum)[0]
#	fileType = file.split('.')[-1]
#	globString = baseName
#	for i in range(0,numPad): globString += '?'
#	theGlob = glob.glob(dir+'\\'+globString+file.split(segNum)[1])
#	numFrames = len(theGlob)
#	firstFrame = theGlob[0]
#	lastFrame = theGlob[-1]
##	return [baseName, numPad, fileType, numFrames, firstFrame, lastFrame]
#	return getSeqInfo("/Volumes/Camilla/DI/_Wrangling/temp_clare/Scripts/_Python_Scripts/_Tree_Scripting/FAB_VFX_PRP0064_20140925")
#
#""pretty tree""

#from os import listdir, sep
#from os.path import abspath, basename, isdir
#from sys import argv
#
#def tree(dir, padding, print_files=False):
#    print padding[:-1] + '+-' + basename(abspath(dir)) + '/'
#    padding = padding + ' '
#    files = []
#    if print_files:
#        files = listdir(dir)
#    else:
#        files = [x for x in listdir(dir) if isdir(dir + sep + x)]
#    count = 0
#    for file in files:
#        count += 1
#        print padding + '|'
#        path = dir + sep + file
#        if isdir(path):
#            if count == len(files):
#                tree(path, padding + ' ', print_files)
#            else:
#                tree(path, padding + '|', print_files)
#        else:
#            print padding + '+-' + file
#
#def usage():
#    return '''Usage: %s [-f] <PATH>
#        Print tree structure of path specified.
#        Options:
#        -f      Print files as well as directories
#        PATH    Path to process''' % basename(argv[0])
#
#def main():
#    if len(argv) == 1:
#        print usage()
#    elif len(argv) == 2:
#        # print just directories
#        path = argv[1]
#        if isdir(path):
#            tree(path, ' ')
#        else:
#            print 'ERROR: \'' + path + '\' is not a directory'
#    elif len(argv) == 3 and argv[1] == '-f':
#        # print directories and files
#        path = argv[2]
#        if isdir(path):
#            tree(path, ' ', True)
#        else:
#            print 'ERROR: \'' + path + '\' is not a directory'
#    else:
#        print usage()
#
#if __name__ == '__main__':
#    main()

#"" Another script for sorting ranges""

#import re
#import glob
#from itertools import groupby
#from operator import itemgetter
#
#def classifyGroups(iterable, reObj=re.compile('\d+')):
#    """Yields successive match lists, where each item in the list is either
#    static text content, or a list of matching values.
#
#     * `iterable` is a list of strings, such as glob('images/*')
#     * `reObj` is a compiled regular expression that describes the
#            variable section of the iterable you want to match and classify
#    """
#    def classify(text, pos=0):
#        """Use a regular expression object to split the text into match and non-match sections"""
#        r = []
#        for m in reObj.finditer(text, pos):
#            m0 = m.start()
#            r.append((False, text[pos:m0]))
#            pos = m.end()
#            r.append((True, text[m0:pos]))
#        r.append((False, text[pos:]))
#        return r
#
#    def matchGrouper(each):
#        """Returns index of matches or origional text for non-matches"""
#        return [(i if t else v) for i,(t,v) in enumerate(each)]
#
#    def unpack(k,matches):
#        """If the key is an integer, unpack the value array from matches"""
#        if isinstance(k, int):
#            k = [m[k][1] for m in matches]
#        return k
#
#    # classify each item into matches
#    matchLists = (classify(t) for t in iterable)
#
#    # group the matches by their static content
#    for key, matches in groupby(matchLists, matchGrouper):
#        matches = list(matches)
#        # Yield a list of content matches.  Each entry is either text
#        # from static content, or a list of matches
#        yield [unpack(k, matches) for k in key]
#        
#        
#def makeResultPretty(res):
#    """Formats data somewhat like the question"""
#    r = []
#    for e in res:
#        if isinstance(e, list):
#            # TODO: collapse and simplify ranges as desired here
#            if len(set(e))<=1:
#                # it's a list of the same element
#                e = e[0]
#            else: 
#                # prettify the list
#                e = '['+' '.join(e)+']'
#        r.append(e)
#    return ''.join(r)
#
#fnList = sorted(glob.glob('images/*'))
#re_digits = re.compile(r'\d+')
#for res in classifyGroups(fnList, re_digits):
#    print makeResultPretty(res)


# ""below script sorts frame ranges""

#!/usr/bin/env python

#import itertools
#import re
#
# This algorithm only works if DATA is sorted.
#DATA = ["image_0001", "image_0002", "image_0003",
#        "image_0010", "image_0011",
#        "image_0011-1", "image_0011-2", "image_0011-3",
#        "image_0100", "image_9999"]
#
#def extract_number(name):
#    # Match the last number in the name and return it as a string,
#    # including leading zeroes (that's important for formatting below).
#    return re.findall(r"\d+$", name)[0]
#
#def collapse_group(group):
#    if len(group) == 1:
#        return group[0][1]  # Unique names collapse to themselves.
#    first = extract_number(group[0][1])  # Fetch range
#    last = extract_number(group[-1][1])  # of this group.
#    # Cheap way to compute the string length of the upper bound,
#    # discarding leading zeroes.
#    length = len(str(int(last)))
#    # Now we have the length of the variable part of the names,
#    # the rest is only formatting.
#    return "%s[%s-%s]" % (group[0][1][:-length],
#        first[-length:], last[-length:])
#
#groups = [collapse_group(tuple(group)) \
#    for key, group in itertools.groupby(enumerate(DATA),
#        lambda(index, name): index - int(extract_number(name)))]
#
#print groups