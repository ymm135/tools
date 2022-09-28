import re

f = open("test.txt")
line = f.readline()
title = ''
while line:
    if len(line) != 0:
        line = line.replace('\n', '')
        matchObj = re.search(r'\(\d+\w\)', line, re.M | re.I)
        print(matchObj)
        if matchObj:
            # 处理时间
            line = line.replace(matchObj.group(0), '').strip()
            line = '引擎C端 >> ' + line
            print(line)

            time = matchObj.group(0).replace('(','').replace(")",'')
            print(time)

    line = f.readline()
f.close()
