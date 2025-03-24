#!/usr/bin/python3

import os
import glob
import sys
import argparse

# syntax
ap = argparse.ArgumentParser(description="show entries list in specified path")
ap.add_argument("-r", "--recursive", action="store_true",
                help="recursively show sub paths")
ap.add_argument("--omit_folder", action="store_true",
                help="omit folders in non-recursive mode")
ap.add_argument("path", nargs="?", default=".",
                help="start path, default is \".\"")
ap.add_argument("-o", "--output", help="output file", default="")
args = ap.parse_args()

# recursive


def listRecursive(root):
    all_files = []
    walk_path = root
    for dir, paths, files in os.walk(walk_path):
        for file in files:
            all_files.append(os.path.join(dir, file))
    all_files.sort()
    return all_files

# no recursive


def listNoRecursive(root, omit_folder):
    cwd = os.getcwd()
    os.chdir(root)
    list = os.listdir()
    list.sort()
    for i in range(len(list), 0, -1):
        if (os.path.isdir(list[i-1])):
            if omit_folder:
                list.pop(i-1)
            else:
                list[i-1] = list[i-1]+"/"
    os.chdir(cwd)
    return list


# execution
entries = []
if args.recursive:
    entries = listRecursive(args.path)
else:
    entries = listNoRecursive(args.path, args.omit_folder)

if args.output == "":
    for e in entries:
        print(e)
else:
    with open(args.output, "w") as f:
        for e in entries:
            f.write(e+"\n")
