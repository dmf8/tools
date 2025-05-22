#!/usr/bin/env python3
import sys
import os
import hashlib
import argparse


def getDataDigest(data, algorithm="sha256"):
    hash = hashlib.new(algorithm)
    hash.update(data)
    return hash.hexdigest()


def getFileDigest(file, algorithm="sha256"):
    with open(file, "rb") as f:
        return getDataDigest(f.read(), algorithm)


ap = argparse.ArgumentParser(description="get hash digest of data/file/folder")
ap.add_argument("-d", "--data")
ap.add_argument("-f", "--file")
ap.add_argument("-p", "--folder")
ap.add_argument("-a", "--algorithm", default="sha256")
args = ap.parse_args()

data = args.data
file = args.file
folder = args.folder
algorithm = args.algorithm

if data == None and file == None and folder == None:
    print("no data provided, exit")
    exit()


if data != None:
    raw = data.encode(encoding="utf-8")
    print(f"algorithm {algorithm}, data digest {getDataDigest(raw,algorithm)}")
elif file != None:
    print(
        f"algorithm {algorithm}, file digest {getFileDigest(file,algorithm)}")
elif folder != None:
    for dir, folders, files in os.walk(folder):
        for file in files:
            path = os.path.join(dir, file)
            print(
                f"file: {path}, {algorithm}: {getFileDigest(path,algorithm)}")
