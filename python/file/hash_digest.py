#!/usr/bin/env python3
import sys
import hashlib
import argparse

ap = argparse.ArgumentParser(description="get hash digest of data or file")
ap.add_argument("-d", "--data")
ap.add_argument("-f", "--file")
ap.add_argument("-a", "--algorithm", default="sha256")
args = ap.parse_args()

data = args.data
file = args.file
algorithm = args.algorithm

if data == None and file == None:
    print("no data or file provided, exit")
    exit()


hash = hashlib.new(algorithm)

if data != None:
    raw = data.encode(encoding="utf-8")
    hash.update(raw)
    print(f"algorithm {algorithm}, data digest {hash.hexdigest()}")
elif file != None:
    with open(file, "rb") as f:
        hash.update(f.read())
        print(f"algorithm {algorithm}, file digest {hash.hexdigest()}")
