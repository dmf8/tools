import argparse
import os

# syntax
parser = argparse.ArgumentParser(
    description="auto add module include and compile info")
parser.add_argument("module", help="module pro relative path")
parser.add_argument("-r", "--root", metavar="",
                    help="project root path, default=.")

args = parser.parse_args()


def priLines(module):
    lines = []
    MODULE = module.upper()
    lines.append("if (!contains(DEFINES, INC_PRI_"+MODULE+")) {\n")
    lines.append("    DEFINES += INC_PRI_"+MODULE+"\n")
    lines.append("    INCLUDEPATH += $${PWD}\n")
    lines.append("\n")
    lines.append("    if (!contains(DEFINES, "+MODULE+"_LIBRARY)) {\n")
    lines.append("        _LIB_NAME_"+MODULE+" = "+module+"\n")
    lines.append("\n")
    lines.append("        win32 {\n")
    lines.append("            CONFIG(debug,debug|release){\n")
    lines.append(
        "                LIBS += -L$${DEBUG_PATH_WIN32} -l$${_LIB_NAME_"+MODULE+"}d\n")
    lines.append("            } else {\n")
    lines.append(
        "                LIBS += -L$${RELEASE_PATH_WIN32} -l$${_LIB_NAME_"+MODULE+"}\n")
    lines.append("            }\n")
    lines.append("        }\n")
    lines.append("\n")
    lines.append("        unix {\n")
    lines.append("            CONFIG(debug,debug|release){\n")
    lines.append("                contains(QT_ARCH, arm64) {\n")
    lines.append(
        "                    LIBS += -L$${DEBUG_PATH_LINUX_ARM64} -l$${_LIB_NAME_"+MODULE+"}d\n")
    lines.append("                } else {\n")
    lines.append(
        "                    LIBS += -L$${DEBUG_PATH_LINUX_X86} -l$${_LIB_NAME_"+MODULE+"}d\n")
    lines.append("                }\n")
    lines.append("            } else {\n")
    lines.append("                contains(QT_ARCH, arm64) {\n")
    lines.append(
        "                    LIBS += -L$${RELEASE_PATH_LINUX_ARM64} -l$${_LIB_NAME_"+MODULE+"}\n")
    lines.append("                } else {\n")
    lines.append(
        "                    LIBS += -L$${RELEASE_PATH_LINUX_X86} -l$${_LIB_NAME_"+MODULE+"}\n")
    lines.append("                }\n")
    lines.append("            }\n")
    lines.append("        }\n")
    lines.append("    }\n")
    lines.append("}\n")
    return lines


def selfIncludeLines(module, module_to_root):
    lines = []
    lines.append("LIB_NAME = "+module+"\n")
    lines.append(
        "PROJECT_ROOT_PATH = $$absolute_path($${_PRO_FILE_PWD_}/"+module_to_root+")\n")
    lines.append(
        "include($$absolute_path($${PROJECT_ROOT_PATH}/common_dest.pri))\n")
    lines.append(
        "include($$absolute_path($${PROJECT_ROOT_PATH}/module_list.pri))\n")
    lines.append("include($${PRI_"+module.upper()+"})\n")
    return lines


# paths
module_pro = args.module
root_path = "."
list_pri = "module_list.pri"
dest_pri = "common_dest.pri"
if args.root != None:
    list_pri = args.root+"/"+list_pri
    dest_pri = args.root+"/"+dest_pri
    root_path = args.root

# get module name
path_split = os.path.split(module_pro)
module_name = os.path.splitext(path_split[1])[0]

pri_file = "ref_"+module_name+".pri"
if path_split[0] != "":
    pri_file = path_split[0]+"/"+pri_file

module_to_root = os.path.relpath(root_path, path_split[0])
root_to_module = os.path.relpath(path_split[0], root_path)

# write
print(f"create module reference pri file {pri_file}")
with open(pri_file, "w") as f:
    f.writelines(priLines(module_name))

print(f"modify module pro file {module_pro}")
with open(module_pro, "a") as f:
    f.writelines(selfIncludeLines(module_name, module_to_root))

print(f"modify list file {list_pri}")
with open(list_pri, "a") as f:
    f.write(
        "PRI_" + module_name.upper() +
        " = $${PROJECT_ROOT_PATH}/" + root_to_module + "/ref_" + module_name + ".pri\n")
