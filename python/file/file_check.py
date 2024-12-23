import os
import glob


def checkExistingFileAbsPath(path):
    if os.path.isfile(path):
        return os.path.abspath(path)
    else:
        return ""


files = glob.glob("t*")
print(files)
