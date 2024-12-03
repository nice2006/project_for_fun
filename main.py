#! python3
# main.py - 主程序入口。
# -*- coding: utf-8 -*-
# time: 2024/11/24

from modules.Translation import translate
from modules.Enc_information import replace_sensitive_information
import os
import sys
import time

def clear_console():
    """
    清理终端屏幕，刷新显示。
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    """
    显示主菜单页面。
    """
    clear_console()
    print("=" * 50)
    print(" 欢迎使用多功能工具程序 ")
    print("=" * 50)
    print("请选择您需要的功能:")
    print("1. 替换文档中的敏感信息 (如电话、邮件地址)")
    print("2. 翻译文本或文件")
    print("0. 退出程序")
    print("=" * 50)

def main():
    """
    主程序入口，负责功能分发。
    """
    try:
        while True:
            show_main_menu()
            choice = input("请输入您的选择 (0-2): ").strip()

            if choice == "1":
                run_replace_sensitive_information()
            elif choice == "2":
                run_translation_tool()
            elif choice == "0":
                print("感谢使用本工具程序，再见！")
                input("按Enter键退出...")
                sys.exit()
            else:
                print("无效选择，请重新输入。")
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序已退出，感谢您的使用！")
        input("按Enter键退出...")

def run_replace_sensitive_information():
    """
    运行敏感信息替换功能，并显示功能主页。
    """
    while True:
        try:
            clear_console()
            print("=" * 50)
            print(" 替换敏感信息 ")
            print("=" * 50)
            print("说明:本功能可以替换 Word 文档中的电话号码和电子邮件地址。")
            print("输入 '0' 返回主菜单。")
            print("=" * 50)

            user_choice = input("是否继续？(Y/n): ").strip().lower()
            if user_choice == "y":
                replace_sensitive_information()
            elif user_choice == "n" or user_choice == "0":
                print("\n返回主菜单...")
                break
            else:
                print("无效输入，请重新选择。")
                time.sleep(1)
        except KeyboardInterrupt:
            break

def run_translation_tool():
    """
    运行翻译功能，并显示功能主页。
    """
    while True:
        try:
            clear_console()
            print("=" * 50)
            print(" 自动翻译工具 ")
            print("=" * 50)
            print("说明:本功能支持翻译文本或文档内容。")
            print("输入 '0' 返回主菜单。")
            print("=" * 50)

            user_choice = input("是否继续？(Y/n): ").strip().lower()
            if user_choice == "y":
                translate()
            elif user_choice == "n" or user_choice == "0":
                print("\n返回主菜单...")
                break
            else:
                print("无效输入，请重新选择。")
                time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
