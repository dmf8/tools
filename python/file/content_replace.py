# args
# 1. origin text
# 2. new text
# 3. files...

# usage
# replace file content of certain pattern in regexp format with given string
# 1. provide the regexp pattern of string to be replaced within ""
# 2. provide the replacement string within ""
# 3. name several files

import sys
import re

str_org = ""
str_replace = ""


def checkLine(line):
    global str_org
    global str_replace
    count = len(re.findall(str_org, line))
    line = re.sub(str_org, str_replace, line)
    return line, count


def handleFile(file):
    lines = []
    with open(file, "r+") as f:
        lines = f.readlines()
        # print(lines)
        count = 0
        for i in range(len(lines)):
            lines[i], temp = checkLine(lines[i])
            count += temp
        print(f"find {count} matches in file {file}")

    with open(file, "w")as f:
        f.writelines(lines)


# args
args = sys.argv
if len(args) < 4:
    print("arguments error")
    exit(0)

str_org = args[1]
str_replace = args[2]
files = args[3:]

# handle each file
for f in files:
    handleFile(f)
