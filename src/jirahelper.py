#!/usr/bin/env python3
"""
This is the main file for JiraHelper
"""
import argparse
import sys
import os
from jira_helper import jirahelper, im_export

def parse_args(argv):
    """
    Parse and document arguments
    """
    default_start_at = 0
    default_max_results = 50

    basename = os.path.basename(argv[0])
    parser = argparse.ArgumentParser(description=f'{basename} - helper script for JIRA')

    group_login = parser.add_argument_group('Login')
    group_login.add_argument(
            '--server',
            type=str,
            required=True,
            help='URL of the JIRA server'
    )
    group_login.add_argument(
            '--user',
            type=str,
            required=True,
            help='Username/email for login'
    )
    group_login_access = group_login.add_mutually_exclusive_group(required=True)
    group_login_access.add_argument(
            '--password',
            type=str,
            help='Password for login'
    )
    group_login_access.add_argument(
            '--token',
            type=str,
            help='Token for login'
    )

    group_action = parser.add_mutually_exclusive_group(required=True)
    group_action.add_argument(
            '--search',
            action='store_true',
            help='JIRA search (JQL)'
    )
    group_action.add_argument(
            '--update',
            action='store_true',
            help='Update by parsing an .xslx file'
    )
    group_action.add_argument(
            '--worklog',
            action='store_true',
            help='Log time for an issue'
    )
    group_action.add_argument(
            '--test',
            action='store_true',
            help='Run in test mode'
    )

    group_jira = parser.add_argument_group('JQL')
    group_jira.add_argument(
            '--jql',
            type=str,
            help='JQL query',
    )
    group_jira.add_argument(
            '--fields',
            type=str,
            help='Fields in the query result',
    )
    group_jira.add_argument(
            '--start_at',
            type=int,
            default=default_start_at,
            help='Start results from offset'
    )
    group_jira.add_argument(
            '--max_results',
            type=int,
            default=default_max_results,
            help='Limit the result (default: 50)'
    )

    group_worklog = parser.add_argument_group('Worklog')
    group_worklog.add_argument(
            '--issue',
            type=str,
            help='Issue ID to log time for',
    )
    group_worklog.add_argument(
            '--time',
            type=str,
            help='Time to log for the issue (e.g. 2d for 2 days)',
    )
    group_worklog.add_argument(
            '--comment',
            type=str,
            help='Comment for worklog'
    )

    group_im_export = parser.add_argument_group('Im-/Export')
    group_im_export.add_argument(
            '--import',
            dest='import_filename',
            type=argparse.FileType('r'),
            help='Import .xslx'
    )
    group_im_export.add_argument(
            '--export',
            type=argparse.FileType('w'),
            help='Export result to .xlsx'
    )

    return parser.parse_args(argv[1:])


def main(argv):
    """
    Main function
    """
    args = parse_args(argv)

    jira = jirahelper.JiraHelper(
            server=args.server,
            username=args.user,
            password=args.password,
            token=args.token
    )
    if args.search:
        results = jira.query(
                args.jql,
                args.fields,
                args.start_at,
                args.max_results
        )
        if args.export:
            im_export.export_query(
                    results,
                    args.fields,
                    args.server,
                    args.export
            )
    elif args.update and args.import_filename:
        data = im_export.import_query(
                args.filename
        )
        jira.update(
                data
        )
    elif args.worklog:
        jira.worklog(
                args.issue,
                args.time,
                args.comment
        )
    else:
        return 1
    return 0


if __name__ == '__main__':
    main(sys.argv)
