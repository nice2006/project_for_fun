#! python3
# regex_utils.py - 定义正则表达式用于匹配电话号码和电子邮件
# -*- coding: utf-8 -*-
# time: 2024/11/24

import re

# 定义正则表达式用于匹配特定格式的电话号码
PhoneRegex = re.compile(r'''
    \d{3}      # 区号
    \d{4}      # 中间部分
    \d{4}      # 最后一部分
''', re.VERBOSE)

# 定义正则表达式用于匹配大部分电子邮件
EmailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+   # 用户名部分
    @                   # @符号
    [a-zA-Z0-9.-]+      # 域名部分
    (\.[a-zA-Z]{2,})+   # 顶级域名，支持多级域名（如 .edu.cn）
''', re.VERBOSE)

def replace_information_in_docx(doc, regex, replacement):
    """
    在 Word 文档中查找并替换内容。
    :param doc: Word 文档对象。
    :param regex: 匹配规则的正则表达式。
    :param replacement: 替换的字符串。
    """
    try:
        for para in doc.paragraphs:
            for run in para.runs:
                if regex.search(run.text):
                    run.text = regex.sub(replacement, run.text)
    except Exception as e:
        print(f"替换内容时发生错误: {e}")
        exit()
