#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : getJira.py
@File    : WriteCSV.py
@Author  : LawrenceYang
@Date    : 2022/7/11 15:49
@Desc    : Null
"""
import os
import csv

baseDir = os.path.split(os.path.dirname(__file__))[0]


def getDesktopPath(resources=False, folder="None"):
    if resources and folder:
        return os.path.join(baseDir, "Resources", folder)
    return os.path.join(os.path.expanduser("~"), 'Desktop')


class WriteCSV():
    def __init__(self, fileName, title=None):
        self.title = ["ID", "类型", "优先级", "报告人", "经办人", "描述", "当前状态", "待办时间", "阻塞时间", "处理中时间", "完成时间",
                      "关闭时间"] if title is None else title
        pathRoad = getDesktopPath(resources=True, folder="csv")
        if not os.path.isdir(pathRoad):
            os.mkdir(pathRoad)

        self.filePath = os.path.join(pathRoad, fileName)
        self.checkExist()

    def checkExist(self):
        if not os.path.isfile(self.filePath):
            obj = self.write()
            f = csv.writer(obj)
            f.writerow(self.title)
            obj.close()

    def write(self):
        return open(self.filePath, "a", newline="")

    def append(self, text):
        self.checkExist()
        obj = self.write()
        f = csv.writer(obj)
        f.writerow(text)
        obj.close()
