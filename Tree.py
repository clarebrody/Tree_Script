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
        print directory
        top_depth = len(os.path.normpath(directory).split(os.sep))
        for parent, sub_dirs, files in os.walk(directory):

            level = len(os.path.normpath(parent).split(os.sep)) - top_depth

            spaces = ' ' * level

            parent = os.path.normpath(parent)
            dir_name = os.path.split(parent)[-1]
            print '%s[%s]' % (spaces, dir_name)

            # filter out hidden files
            filtered = [x for x in files if not x.startswith('.')]

            if args.extensions:
                filtered = [x for x in filtered if os.path.splitext(x)[1].lower() in args.extensions]

            for filename in filtered:
                print spaces + ' ' + filename


def main():
    args = command_line_args()
    walker(args)

if __name__ == '__main__':
    main()