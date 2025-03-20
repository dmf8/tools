import os
import sys

this_file=sys.argv[0]

raw_list=os.listdir()
raw_list.sort()
print(raw_list)

for i in range(len(raw_list),0,-1):
    j=i-1
    if this_file==raw_list[j]:
        print(j)
        raw_list.pop(j)

print(raw_list)