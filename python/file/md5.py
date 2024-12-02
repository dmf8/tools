import sys
import hashlib

args = sys.argv
if len(args) < 2:
    print("no file appointed")
    exit(0)

print(f"md5 of \"{args[1]}\"")
f = open(args[1], "rb")

print(hashlib.md5(f.read()).hexdigest())
