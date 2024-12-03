#! python3
# get_path.py - 获取文件路径
# -*- coding: utf-8 -*-
# time: 2024/11/24

import os
from .path_utils import clean_path

def get_file_path(prompt, is_input=True):
    """
    通用函数:获取文件路径。
    :param prompt: 提示信息。
    :param is_input: 是否为输入文件路径 (默认是 True)。
        - 如果为 True，检查路径是否有效。
        - 如果为 False，处理输出路径，若存在则询问是否覆盖。
    :return: 绝对路径。
    """
    while True:
        try:
            file_path = input(prompt).strip()
            file_path = os.path.abspath(clean_path(file_path))

            if is_input:
                if os.path.exists(file_path):
                    return file_path
                else:
                    print("输入的文件路径无效，请检查后重试。")
            else:
                if os.path.exists(file_path):
                    overwrite = input(f"输出文件 '{file_path}' 已存在，是否覆盖？(Y/n): ").strip().lower()
                    if overwrite == 'y':
                        return file_path
                    elif overwrite == 'n':
                        continue
                    else:
                        print("无效的输入，请输入 'Y' 或 'n'。")
                else:
                    return file_path
        except KeyboardInterrupt:
            return None
        except Exception as e:
            print(f"发生错误:{e}")
            input("按下回车键退出程序...")
            exit()

def get_output_path(default_ext):
    """
    获取用户提供的输出文件路径。
    :param default_ext: 默认的文件扩展名 (.txt 或 .docx)。
    :return: 输出文件路径。
    """
    try:
        output_path = input(f"请输入输出文件路径(以 {default_ext} 结尾):").strip()
        if not output_path:
            print("未提供输出路径，操作取消。")
            return None

        output_path = clean_path(output_path)
        if not output_path.endswith(default_ext):
            output_path += default_ext

        # 转换为跨平台绝对路径
        output_path = os.path.abspath(output_path)

        # 如果目录不存在，则创建
        parent_dir = os.path.dirname(output_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        return output_path
    except KeyboardInterrupt:
        return None
