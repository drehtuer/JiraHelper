"""
Unit test for jirahelper.py
"""
import sys
import unittest
import settings
import jirahelper


class TestJirahelperMethods(unittest.TestCase):
    """
    Test class for jirahelper.py
    """

    def test_parse_args(self):
        """
        Test jirahelper.parse_args(argv)
        """
        args = jirahelper.parse_args(
                [
                    sys.argv[0],
                    '--server', settings.SERVER,
                    '--user', settings.USER,
                    '--token', settings.TOKEN,
                    '--test'
                ]
        )
        self.assertEqual(args.server, settings.SERVER)
        self.assertEqual(args.user, settings.USER)
        self.assertEqual(args.token, settings.TOKEN)


    def test_main(self):
        """
        Test jirahelper.parse_main(argv)
        """
        result = jirahelper.main(
                [
                    sys.argv[0],
                    '--server', settings.SERVER,
                    '--user', settings.USER,
                    '--token', settings.TOKEN,
                    '--test'
                ]
        )
        self.assertEqual(result, 1)
