#!/usr/bin/env python

import argparse
import os


def command_line_args():
    parser = argparse.ArgumentParser(description='Directory tree script')
    parser.add_argument('--extensions', '-e', action='store', nargs='*')
    parser.add_argument('directories', action='store', nargs='+')

    return parser.parse_args()


def walker(args):
    for directory in args.directories:
        for parent, sub_dirs, files in os.walk(directory):
            print parent, sub_dirs, files

def main():
    args = command_line_args()
    walker(args)

if __name__ == '__main__':
    main()