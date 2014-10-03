#!/usr/bin/env python

import argparse


def command_line_args():
    parser = argparse.ArgumentParser(description='Short sample app')

    parser.add_argument('directories', action='store', nargs='+', type=str)

    return parser.parse_args()


def main():
    args = command_line_args()
    print args

if __name__ == '__main__':
    main()