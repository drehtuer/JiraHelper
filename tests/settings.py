"""
Settings for unit test to connect to your JIRA instance
"""
SERVER='<JIRA instance URL>'
USER='drehtuer@drehtuer.de'
PASSWORD='<plain text password or None>'
TOKEN='<access token or None>'

"""
Settings for test cases
"""

# jira_helper/JiraHelper.query
TEST_QUERY_JQL='project=<your project>'
TEST_QUERY_FIELDS=['created', 'updated']

# jira_helper/JiraHelper.worklog
TEST_WORKLOG_ISSUE='<story>'
TEST_WORKLOG_TIME='2h'
TEST_WORKLOG_COMMENT='Test comment'
