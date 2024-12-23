# args
# 1. origin text
# 2. new text
# 3. files...


import sys

str_org = ""
str_replace = ""


def checkLine(line):
    return True


def tryReplaceLine(line):
    pass


def handleFile(file):
    lines = []
    with open(file, "r+") as f:
        lines = f.readlines()
        print(lines)
        for i in range(len(lines)):
            tryReplaceLine(lines[i])
            if checkLine(lines[i]):
                lines[i] = "replace\n"

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

# file check


# handle each file
for f in files:
    handleFile(f)
