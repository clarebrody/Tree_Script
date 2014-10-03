#!/usr/bin/env python

import os
#for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#        print(os.path.join(root, name))
#    for name in dirs:
#        print(os.path.join(root, name))
#        
#    
#import os
#for root, dirs, files in os.walk(os.path.abspath(".")):
#  for file in files:
#    print os.path.join(root, file)
#    print sort(os.path.join(root, file))
#
#import fnmatch
#import os
# 
#rootPath = '.'
#pattern = '*.dpx'
# 
#for root, dirs, files in os.walk(rootPath):
#    for filename in fnmatch.filter(files, pattern):
#        print( os.path.join(root, filename))
#        
#def find_missing_range(my_numbers, range_min, range_max):
#    expected_range = set(range(range_min, range_max + 1))
#    return expected_range - set(my_numbers)
#
#def numbers_as_ranges(numbers):
#    ranges = []
#    for number in numbers:
#        if ranges and number == (ranges[-1][-1] + 1):
#            ranges[-1] = (ranges[-1][0], number)
#        else:
#            ranges.append((number, number))
#    return ranges
#
#def format_ranges(ranges):
#    range_iter = (("%d" % r[0] if r[0] == r[1] else "%d-%d" % r) for r in ranges)
#    return "(" + ", ".join(range_iter) + ")"
#
#def main(my_numbers, range_min, range_max):
#    numbers_missing = find_missing_range(my_numbers, range_min, range_max)
#    ranges = numbers_as_ranges(numbers_missing)
#    return format_ranges(ranges)
#
#if __name__ == '__main__':
#    range_min, range_max = 1, 40
#    print main([1, 4, 6, 10, 12], range_min, range_max)
#    print main([1, 2, 3, 4, 10, 20], range_min, range_max)