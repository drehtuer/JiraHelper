"""
Unit test for jirahelper.py
"""
import sys
import unittest
import jirahelper


class TestJirahelperMethods(unittest.TestCase):
    """
    Test class for jirahelper.py
    """

    def test_parse_args(self):
        """
        Test jirahelper.parse_args(argv)
        """
        server='testserver'
        user='testuser'
        password='testpass'
        args = jirahelper.parse_args(
                [
                    sys.argv[0],
                    '--server', server,
                    '--user', user,
                    '--password', password
                ]
        )
        self.assertEqual(args.server, server)
        self.assertEqual(args.user, user)
        self.assertEqual(args.password, password)
