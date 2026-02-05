# 代码片段汇总表
## cpp
|prefix|description|
|-|-|
|myheader|header guard & class name|
|mycpp|header include and class name|
|iostream|include and using namespace std|

## cmake
|prefix|description|
|-|-|

# vscode配置流程
1. 在菜单中找到入口

    File/Preferences/Configure User Snippets

1. 打开或新建一个json配置文件
    
    配置按照不同的语言分文件存放, 如python.json

    - 已经存在的*.json文件会出现在下方列表中
    - 不存在的语言可以在输入框中输入语言名进行创建

1. 根据案例, 在根对象中创建或编辑json对象

    以一个案例来解释json对象的字段

    ```json
    "Create .h file": { //json对象名, 是一个说明字符串
		"prefix": "myheader", //用于呼出snippet的关键字
		"body": [ //片段的具体内容, 每对双引号表示一行内容
			"#ifndef ${1:HEADER_NAME}_H",
			"#define ${1:HEADER_NAME}_H\n",
			"class ${2:ClassName} {",
			"public:",
			"    ${2:ClassName}();",
			"    ~${2:ClassName}();",
			"};",
			"#endif // ${1:HEADER_NAME}_H"
		],
		"description": "Create a new header file with basic class structure",
        "scope": "" //
	}
    ```