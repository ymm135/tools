#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : netproto
@File    : getJira.py
@Author  : LawrenceYang
@Date    : 2022/6/30 10:47
@Desc    : Null
"""

from jira import JIRA
from collections import Counter
from WriteCSV import WriteCSV
import re


def getJira(jiraUrl, username, password, jql):
    '''
    获取jira的数据
    :param jiraUrl:   jira的url
    :param username:  用户名
    :param password:  密码
    :param jql:       查询的jql
    :return:
    '''
    jira = JIRA(server=jiraUrl, basic_auth=(username, password))
    issues = jira.search_issues(jql, expand="changelog", maxResults=-1)
    issues_msg = []
    for issue in issues:
        issue_msg = [''] * 12
        # "ID", "类型", "优先级", "报告人", "经办人", "描述", "当前状态", "待办时间", "阻塞时间", "处理中时间", "完成时间", "关闭时间"
        issue_msg[0] = issue.key
        issue_msg[1] = issue.fields.issuetype.name
        issue_msg[2] = issue.fields.priority.name
        issue_msg[3] = issue.fields.reporter.displayName
        issue_msg[4] = issue.fields.reporter.displayName if issue.fields.assignee is None else issue.fields.assignee.displayName
        issue_msg[5] = issue.fields.summary
        issue_msg[6] = issue.fields.status.name
        issue_msg[7] = issue.fields.created.split("T")[0]
        for history in issue.changelog.histories:
            if history.items[0].field == "status":
                if history.items[0].toString == "打开":
                    issue_msg[7] = history.created.split("T")[0]
                elif history.items[0].toString == "阻塞":
                    issue_msg[8] = history.created.split("T")[0]
                elif history.items[0].toString == "处理中":
                    issue_msg[9] = history.created.split("T")[0]
                elif history.items[0].toString == "待验证":
                    issue_msg[10] = history.created.split("T")[0]
                elif history.items[0].toString == "关闭":
                    issue_msg[11] = history.created.split("T")[0]
        issues_msg.append(issue_msg)
    return issues_msg


def get_func_frequency(file_path):
    funcs_list = []
    with open(file_path) as f:
        for line in f.readlines():
            try:
                func = re.findall(r'\s[A-z0-9+.]*\s\(', line)
                funcs_list.append(func[0].lstrip().strip(' ('))
            except:
                continue
    count = Counter(funcs_list)
    count_dict = dict(count)
    # print(count_dict)
    return count_dict


if __name__ == "__main__":
    jiraUrl = "http://10.25.10.110:8092"
    # jql = 'project = "AUDIT" AND issuetype = 故障 ORDER BY priority DESC, updated DESC'
    jql = 'project = "AUDIT" AND issuetype in (任务, 子任务)'
    issues_msg = getJira(jiraUrl, 'yangmingming', 'Netvine123', jql=jql)
    for issue in issues_msg:
        WriteCSV("jira_issues.csv").append(issue)

