#!/usr/bin/env python3

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
args = ap.parse_args()

# recursive


def listRecursive(root):
    all_files = []
    walk_path = root
    for dir, paths, files in os.walk(walk_path):
        for file in files:
            full_path = os.path.join(dir, file)
            size = os.path.getsize(full_path)
            all_files.append((full_path, size))
    all_files.sort(key=lambda x: x[0])
    return all_files

# no recursive


def listNoRecursive(root, omit_folder):
    cwd = os.getcwd()
    os.chdir(root)
    list = os.listdir()
    list.sort()
    result = []
    for i in range(len(list), 0, -1):
        if (os.path.isdir(list[i-1])):
            if omit_folder:
                pass
            else:
                result.append((list[i-1]+"/", 0))
        else:
            size = os.path.getsize(list[i-1])
            result.append((list[i-1], size))
    os.chdir(cwd)
    result.sort(key=lambda x: x[0])
    return result


# execution
entries = []
if args.recursive:
    entries = listRecursive(args.path)
else:
    entries = listNoRecursive(args.path, args.omit_folder)

for e in entries:
    print(f"{e[1]},{e[0]}")

