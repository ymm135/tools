from jira import JIRA
import re

username = "yangmingming"
password = "711214"


def UpdateTimetracking(issue, original=None):
    issue.update(fields={'timeoriginalestimate': original})


def CreateTask(summary, timeoriginalestimate):
    issue_dict = {
        'project': project,
        'summary': 'Testing custom field',
        'description': '',
        'issuetype': '故事',
        'labels': ['防火墙-自动化创建']
    }

    issue_dict['summary'] = summary
    issue_dict['issuetype'] = '任务'
    new_task = jira.create_issue(fields=issue_dict)
    print(summary + new_task.key)

    # UpdateTimetracking(new_task,original=timeoriginalestimate)


jira = JIRA('http://10.25.10.110:8092', basic_auth=(username, password))

project = "FIREWALL"

# 创建任务
f = open("test.txt")
line = f.readline()
while line:
    if len(line) != 0:
        line = line.replace('\n', '').strip()
        # matchObj = re.search(r'\(\d+\w\)', line, re.M | re.I)
        # print(matchObj)
        # if matchObj:
        # 处理时间
        # line = line.replace(matchObj.group(0), '').strip()
        line = '引擎C端 >> ' + line
        print(line)
        CreateTask(line, '')
    line = f.readline()
f.close()
