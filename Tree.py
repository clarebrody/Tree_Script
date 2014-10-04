#!/usr/bin/env python

import argparse
import os


def command_line_args():
    parser = argparse.ArgumentParser(description='Directory tree script')
    parser.add_argument('--extensions', '-e', action='store', nargs='*')
    parser.add_argument('directories', action='store', nargs='+')

    return parser.parse_args()


def get_directory_level(dir_name):
    clean_path = os.path.normpath(dir_name)
    split_dirs = clean_path.split(os.sep)
    return len(split_dirs)


def range_summary(files):

    sort_files = sorted(files)

    file_ranges = []

    start = None
    previous = None
    start_frame = None
    end_frame = None

    for idx, filename in enumerate(sort_files):
        name, extension = os.path.splitext(filename)

        if len(sort_files) == 1:
            file_ranges.append((sort_files[0], sort_files[0]))
            break

        if idx == 0:
            start = name
            previous = name

        else:

            common_part = os.path.commonprefix([name, start])
            previous_file_digit = previous[len(common_part):]
            current_file_digit = name[len(common_part):]

            count_diff = 0
            try:
                count_diff = int(current_file_digit) - int(previous_file_digit)
            except ValueError:
                start = name

            print '  yy', previous, name, count_diff
            if count_diff != 1:
                file_ranges.append((start, previous))

                start = name

            if idx == len(sort_files) - 1:
                print 'resetting'
                file_ranges.append((start, name))

                start = name

            previous = name

    print file_ranges
    return file_ranges


def walker(args):

    for directory in args.directories:
        print directory
        top_dir_level = get_directory_level(directory)
        for parent, sub_dirs, files in os.walk(directory):

            level = get_directory_level(parent) - top_dir_level

            spaces = ' ' * level

            parent = os.path.normpath(parent)
            dir_name = os.path.split(parent)[-1]
            print '%s[%s]' % (spaces, dir_name)

            # filter out hidden files
            filtered = [x for x in files if not x.startswith('.')]

            if args.extensions:
                filtered = [x for x in filtered if os.path.splitext(x)[1].lower() in args.extensions]

            # range_summary(filtered)
            for file_ranges in range_summary(filtered):
                pass
               #print spaces + ' ' + str(file_ranges)


def main():
    args = command_line_args()
    walker(args)

if __name__ == '__main__':
    main()