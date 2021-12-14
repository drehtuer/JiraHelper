#!/usr/bin/env python3
"""
This is the main file for JiraHelper
"""
import argparse
import sys
import os


def parse_args(argv):
    """
    Parse and document arguments
    """
    basename = os.path.basename(argv[0])
    parser = argparse.ArgumentParser(description=f'{basename} - helper script for JIRA')

    group_login = parser.add_argument_group('Login')
    group_login.add_argument(
            '--server',
            type=str,
            required=True
    )
    group_login.add_argument(
            '--user',
            type=str,
            required=True
    )
    group_login.add_argument(
            '--password',
            type=str,
            required=True
    )

    group_jira = parser.add_argument_group('JIRA')
    group_jira.add_argument(
            '--jql',
            type=str
    )

    group_im_export = parser.add_argument_group('Im-/Export')
    group_im_export.add_argument(
            '--import',
            type=argparse.FileType('r')
    )
    group_im_export.add_argument(
            '--export',
            type=argparse.FileType('w')
    )

    return parser.parse_args(argv[1:])


def main(argv):
    """
    Main function
    """
    parse_args(argv)


if __name__ == '__main__':
    main(sys.argv)
