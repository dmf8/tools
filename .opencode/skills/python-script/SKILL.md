---
name: python-script
description: 在当前项目python/目录下创建Python脚本。根据用户定义的脚本名称（可包含目录名如 `dir/script`）创建对应的py文件，自动递归创建子目录。适用于需要创建新Python脚本的场景。
---

# Python Script Creator

## 基本工作流程

1. **解析脚本名称**: 获取用户定义的脚本名称（去掉.py后缀）
2. **确定目标目录**: 目标基础目录为当前项目根目录下的 `python/`
3. **递归创建目录**: 如果名称包含子目录（如 `network/http_request`），先递归创建所有父目录
4. **创建脚本文件**: 在正确位置创建同名 .py 文件

## 使用示例

用户请求:
- `创建一个叫 network/network_info 的脚本` → 创建 `python/network/network_info.py`
- `创建一个叫 file/hash_digest 的脚本` → 创建 `python/file/hash_digest.py`
- `创建一个叫 utils 的脚本` → 创建 `python/utils.py`

## 脚本模板

创建脚本时使用以下模板:

```python
#!/usr/bin/env python3
"""
[脚本名称] - [简短描述]

Usage:
    python [脚本名].py [参数]

Args:
    [参数说明]
"""

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="[描述]")
    parser.add_argument("-i", "--input", type=Path, help="输入文件")
    parser.add_argument("-o", "--output", type=Path, help="输出文件")
    parser.add_argument("args", nargs="*", help="其他参数")
    args = parser.parse_args()
    
    # TODO: 实现脚本逻辑


if __name__ == "__main__":
    main()
```

## 注意事项

- 脚本名可以包含路径分隔符 `/`，会自动创建子目录
- 基础目录固定为 `{workspace_root}/python/`
- 创建完成后需添加执行权限: `chmod +x <script_path>`
- 参考现有脚本的风格: `python/file/`, `python/network/`, `python/interaction/`

## 参考案例
- `{workspace_root}/python/network/network_info.py`