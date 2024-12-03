#! python3
# Enc_Information.py - 加密主程序
# -*- coding: utf-8 -*-
# time: 2024/11/24

from .get_path import get_file_path
from .regex_utils import PhoneRegex, EmailRegex, replace_information_in_docx
from docx import Document
import os

def clear_console():
    """
    清理终端屏幕，刷新显示。
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_replacement_string(replace_target):
    """
    获取用户提供的替换字符串。
    :param replace_target: 替换目标名称。
    :return: 用户输入的替换字符串。
    """
    try:
        return input(f"请输入用于替换 {replace_target} 的字符串:").strip()
    except KeyboardInterrupt:
        raise  # 重新抛出异常以在主流程中处理

def ask_user_if_replace(target_name):
    """
    询问用户是否替换特定类型的信息。
    :param target_name: 替换目标名称（如电子邮件、电话号码）。
    :return: 如果用户选择 'Y' 返回 True，否则返回 False。
    """
    try:
        response = input(f"是否需要替换 {target_name}？(Y/n):").strip().lower()
        return response == 'y'
    except KeyboardInterrupt:
        raise  # 重新抛出异常以在主流程中处理

def replace_sensitive_information():
    """
    替换 Word 文档中的敏感信息（如电子邮件和电话号码）。
    """
    while True:
        try:
            clear_console()
            print("=" * 50)
            print(" 替换敏感信息 ")
            print("=" * 50)
            print("说明：本功能可以替换 Word 文档中的电话号码和电子邮件地址。")
            print("=" * 50)

            # 用户选择是否替换电子邮件和电话号码
            replace_email = input("是否需要替换 电子邮件？(Y/n): ").strip().lower() == "y"
            replace_phone = input("是否需要替换 电话号码？(Y/n): ").strip().lower() == "y"

            if not replace_email and not replace_phone:
                print("\n未选择任何替换，返回主菜单。")
                input("按回车键继续...")
                return  # 返回主菜单

            # 获取输入文件路径
            input_file = get_file_path("请输入需要替换的 Word 文件路径: ", is_input=True)
            if input_file is None:  # 用户中断或输入 '0'
                return

            # 获取输出文件路径
            output_file = get_file_path("请输入输出文件路径(以 .docx 结尾): ", is_input=False)
            if output_file is None:  # 用户中断或输入 '0'
                return
            # 替换敏感信息
            try:
                doc = Document(input_file)

                if replace_email:
                    email_replacement = input("请输入用于替换电子邮件的字符串: ").strip()
                    replace_information_in_docx(doc, EmailRegex, email_replacement)

                if replace_phone:
                    phone_replacement = input("请输入用于替换电话号码的字符串: ").strip()
                    replace_information_in_docx(doc, PhoneRegex, phone_replacement)

                doc.save(output_file)
                print(f"\n替换完成，文档已保存至: {output_file}")

            except PermissionError:
                print(f"\n保存失败：没有权限写入文件 {output_file}，请检查文件是否被占用。")
            except Exception as e:
                print(f"\n替换过程中发生错误: {e}")

            input("\n按回车键返回主菜单...")
            return

        except KeyboardInterrupt:
            return