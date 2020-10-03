from jira import JIRA
def connect(uid,pwd):
    global jira
    jira_server = "https://jira.domain.com"
    jira_server = {'server': jira_server}
    jira = JIRA(options=jira_server, basic_auth=(uid, pwd))
    return jira
