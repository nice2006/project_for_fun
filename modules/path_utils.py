#! python3
# path_utils.py - 消除路径中的引号
# -*- coding: utf-8 -*-
# time: 2024/11/24

def clean_path(path):
    """
    清理文件路径，移除开头和结尾的引号。
    :param path: 用户输入的文件路径。
    :return: 清理后的文件路径。
    """
    if (path.startswith('"') and path.endswith('"')) or (path.startswith("'") and path.endswith("'")):
        return path[1:-1]
    return path
