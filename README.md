# Python project_for_fun

## 项目简介
这是一个多功能文本处理工具，主要提供文档敏感信息替换和多语言翻译功能。

## 功能特点
- 文档敏感信息替换
  - 支持替换文档中的电话号码（11位）
  - 支持替换文档中的电子邮件地址
  - 支持自定义替换文本
- 多语言翻译功能
  - 支持文本直接翻译
  - 支持文件翻译（.txt 和 .docx 格式）
  - 支持多种语言之间的互译
  - 自动检测源语言

## 环境要求
- Python 3.x
- 依赖包：
  - python-docx
  - googletrans
  - os
  - re
  - sys
  - time

## 安装说明 
```bash
git clone https://github.com/nice2006/project_for_fun.git
cd project_for_fun
pip install -r requirements.txt
```

## 使用说明
### 基本使用
```bash
python main.py
```

### 功能详解
1. 敏感信息替换功能
   - 选择主菜单中的选项 1
   - 选择是否需要替换电子邮件和电话号码
   - 输入源文件路径（支持 .docx 格式）
   - 输入目标文件保存路径
   - 输入替换文本
   - 程序将自动完成替换并保存

2. 文本翻译功能
   - 选择主菜单中的选项 2
   - 设置目标语言代码（默认为中文 zh-cn）
   - 选择翻译模式：
     - 文本翻译：直接输入文本进行翻译
     - 文件翻译：支持 .txt 和 .docx 格式
   
### 支持的语言代码
常用语言代码示例：
- 中文（简体）: zh-cn
- 中文（繁体）: zh-tw
- 英语: en
- 日语: ja
- 韩语: ko
- 法语: fr
- 德语: de
- 西班牙语: es
...更多语言代码请在程序中查看

### 文件格式支持
- 敏感信息替换：支持 .docx 格式
- 文本翻译：支持 .txt 和 .docx 格式

## 项目结构
```
project_for_fun/
├── main.py                    # 主程序入口
├── modules/                   # 模块目录
│   ├── Enc_information.py    # 敏感信息处理模块
│   ├── Translation.py        # 翻译功能主模块
│   ├── translate_module.py   # 翻译核心模块
│   ├── get_path.py          # 路径处理模块
│   ├── path_utils.py        # 路径工具模块
│   └── regex_utils.py       # 正则表达式工具模块
├── README.md                 # 项目说明文档
└── LICENSE                   # 许可证文件
```

## 贡献指南
欢迎提交 Pull Request 来改进这个项目。

1. Fork 这个项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m '添加了一些特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证
本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情