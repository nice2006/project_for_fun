#! python3
# Translation.py - 翻译主程序
# -*- coding: utf-8 -*-
# time: 2024/11/24

import os
import time
from .translate_module import translate_text, translate_file
from .get_path import get_file_path, get_output_path

def clear_console():
    """
    清理终端屏幕，刷新显示。
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_language_codes():
    """
    显示常用语言代码。
    """
    print(" 常用语言及其代码 ")
    print("=" * 50)
    print("| 语言          | 语言代码  |")
    print("|---------------|-----------|")
    print("| 中文（简体）  | zh-cn     |")
    print("| 中文（繁体）  | zh-tw     |")
    print("| 英语          | en        |")
    print("| 法语          | fr        |")
    print("| 德语          | de        |")
    print("| 日语          | ja        |")
    print("| 韩语          | ko        |")
    print("| 西班牙语      | es        |")
    print("| 意大利语      | it        |")
    print("| 葡萄牙语      | pt        |")
    print("| 俄语          | ru        |")
    print("| 阿拉伯语      | ar        |")
    print("| 印地语        | hi        |")
    print("| 泰语          | th        |")
    print("| 越南语        | vi        |")
    print("| 马来语        | ms        |")
    print("| 土耳其语      | tr        |")
    print("| 乌克兰语      | uk        |")
    print("| 波兰语        | pl        |")
    print("| 荷兰语        | nl        |")
    print("| 希腊语        | el        |")
    print("| 瑞典语        | sv        |")
    print("| 捷克语        | cs        |")
    print("| 罗马尼亚语    | ro        |")
    print("| 匈牙利语      | hu        |")
    print("| 芬兰语        | fi        |")
    print("| 丹麦语        | da        |")
    print("| 挪威语        | no        |")
    print("=" * 50)

def translate():
    """
    提供翻译功能的界面交互。
    """
    try:
        clear_console()
        print("=" * 50)
        print(" 欢迎使用自动化翻译工具 ")
        print("=" * 50)
        print("说明:请先设置翻译目标语言，稍后可直接开始翻译。")
        print("=" * 50)
        display_language_codes()
        target_language = input("请输入目标语言代码（如 'zh-cn' 中文）:").strip() or "zh-cn"
    except KeyboardInterrupt:
        return  # 返回主页面

    while True:
        try:
            clear_console()
            print("=" * 50)
            print(" 自动翻译工具 ")
            print("=" * 50)
            print(f"当前翻译目标语言: {target_language}")
            print("请选择您需要的功能:")
            print("1. 翻译文本")
            print("2. 翻译文件")
            print("0. 返回主菜单")
            print("=" * 50)

            choice = input("请输入您的选择 (0-2):").strip()

            if choice == "1":
                # 翻译文本
                text = input("请输入需要翻译的文本:").strip()
                try:
                    result, detected_lang = translate_text(text, target_language)
                    print(f"\n检测到的语言: {detected_lang}")
                    print("翻译结果:")
                    print(result)
                except Exception as e:
                    print(f"翻译失败: {e}")
                input("\n按回车键继续...")  # 暂停等待用户查看结果

            elif choice == "2":
                # 翻译文件
                input_file = get_file_path("请输入需要翻译的文件路径:", is_input=True)
                if input_file is None:  # 用户中断或输入 '0'
                    return
                default_ext = ".docx" if input_file.endswith(".docx") else ".txt"
                output_file = get_output_path(default_ext)
                if output_file is None:  # 用户中断或输入 '0'
                    return

                try:
                    translate_file(input_file, output_file, target_language)
                    print(f"翻译已完成，保存到: {output_file}")
                except Exception as e:
                    print(f"文件翻译失败: {e}")
                input("\n按回车键继续...")  # 暂停等待用户查看结果

            elif choice == "0":
                break
            else:
                print("无效选择，请重新输入。")
                input("\n按回车键继续...")  # 暂停等待用户查看错误提示

        except KeyboardInterrupt:
            break  # 返回主页面
