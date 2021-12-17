"""
JIRA wrapper class
"""
import jira

# Some fields cannot be updated, but must be handled differently,
# e.g. via a transition.
FIELDS_NO_UPDATE = [
        'key',
        'status'
]


class JiraHelper():
    """
    Login for JIRA
    Creates the JIRA object
    """

    def __init__(self, server, username, password, token):
        """
        CTOR for Jira class
        Connects to JIRA server
        """
        if password is not None:
            auth=(
                    username,
                    password
            )
        elif token is not None:
            auth=(
                    username,
                    token
            )
        else:
            raise RuntimeError('Neither password nor token given')

        self._jira = jira.JIRA(
               server=server,
               basic_auth=auth
        )


    def close(self):
        """
        Close connection to JIRA
        """
        self._jira.close()


    def query(self, jql, fields, start_at=0, max_results=50):
        """
        Run a JQL query
        """
        result = self._jira.search_issues(
                jql_str=jql,
                fields=fields,
                startAt=start_at,
                maxResults=max_results,
                json_result=True
        )
        return self._parse_results(result)


    def worklog(self, issue, time, comment):
        """
        Add worklog
        """
        worklog = self._jira.add_worklog(
                issue=issue,
                timeSpent=time,
                comment=comment
        )
        return self._parse_worklog(worklog.raw)


    def update(self, results):
        """
        Update JIRA from data
        """
        new_results = []
        try:
            for result in results:
                if result['key'] or result['key'] == '':
                    print(f'Updating issue \'{result["key"]}\' ...')
                    issue = self._jira.issue(result['key'])
                    pop_fields = [item for item in result if item in FIELDS_NO_UPDATE]
                    for field in pop_fields:
                        result.pop(field)
                    new_results.append(issue.update(
                            fields=result,
                            notify=True
                    ))
        except jira.exceptions.JIRAError as exception:
            print(exception)
            return False
        return True


    @staticmethod
    def _parse_results(result_dict):
        """
        Convert result json in easier readable format
        """
        result = []
        for issue in result_dict['issues']:
            parsed = {
                    'key': issue['key']
            }
            for fields, value in issue['fields'].items():
                parsed[fields] = value
            result.append(parsed)
        return result


    @staticmethod
    def _parse_worklog(worklog):
        """
        Convert worklog in easier readable format
        """
        return {
                'author': worklog['author']['displayName'],
                'time': worklog['timeSpent'],
                'comment': worklog['comment']
        }
