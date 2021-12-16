"""
Unit tests for jira_helper/jirahelper.py
"""
import unittest
import settings
from jira_helper import jirahelper

class TestJiraHelperJiraHelperMethods(unittest.TestCase):
    """
    Test class for jira_helper/jirahelper.py
    """


    def setUp(self):
        """
        SetUp: Create connection to JIRA server
        """
        self._jira = jirahelper.JiraHelper(
                server = settings.SERVER,
                username = settings.USER,
                password = settings.PASSWORD,
                token = settings.TOKEN
        )


    def tearDown(self):
        """
        TearDown: Close connection to JIRA server
        """
        self._jira.close()


    def test_close(self):
        """
        Test JiraHelper.close()
        """
        self._jira.close()


    def test_query(self):
        """
        Test JiraHelper.query(jql, fields, max_results)
        """
        result = self._jira.query(
                settings.TEST_QUERY_JQL,
                settings.TEST_QUERY_FIELDS
        )
        print(result)
        for row in result:
            for field in settings.TEST_QUERY_FIELDS:
                self.assertIn(field, row)


    def test_worklog(self):
        """
        Test JiraHelper.worklog(issue, time, comment)
        """
        worklog = self._jira.worklog(
                settings.TEST_WORKLOG_ISSUE,
                settings.TEST_WORKLOG_TIME,
                settings.TEST_WORKLOG_COMMENT
        )
        print(worklog)
        self.assertEqual(worklog['time'], settings.TEST_WORKLOG_TIME)
        self.assertEqual(worklog['comment'], settings.TEST_WORKLOG_COMMENT)
