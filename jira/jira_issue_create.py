from jira import JIRA
import re

username = "yangmingming"
password = "711214"



def CreateTask(summary):
    issue_dict = {
        'project': project,
        'summary': 'Testing custom field',
        'description': '',
        'issuetype': '故事',
        'labels': ['防火墙-自动化创建']
    }

    issue_dict['summary'] = summary
    issue_dict['issuetype'] = '故事'

    new_story = jira.create_issue(fields=issue_dict)
    print(new_story.key)

    issue_dict['issuetype'] = '任务'
    new_task = jira.create_issue(fields=issue_dict)
    print(new_story.key)


    # 将任务关联需求
    # inwardIssue 需求的key
    jira.create_issue_link(type='relates to', outwardIssue=new_task.key, inwardIssue=new_story.key)


jira = JIRA('http://10.25.10.110:8092', basic_auth=(username, password))

# 搜索查询
# jql = "project = FIREWALL AND resolution = Unresolved and id = FIREWALL-68"
# issue = jira.search_issues(jql, expand="changelog", maxResults=-1)
# print(issue)

project = "FIREWALL"
# 创建任务

f = open("目录.txt")
line = f.readline()
title = ''
while line:
    if len(line) != 0:
        line = line.replace('\n', '')
        matchObj = re.search(r'\.\d\.', line, re.M | re.I)
        if matchObj:
            # 二级
            summary = title + ' >> ' + line
            print(summary)
            CreateTask(summary)
        else:
            # 一级
            # print(line)
            title = line
    line = f.readline()
f.close()


