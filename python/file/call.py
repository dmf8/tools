import file_check

content = ""
with open("ade", "r") as f:
    content = f.read()

with open("xxx", "w") as f:
    f.write(content)
