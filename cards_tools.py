"""
创建一个简单的名片管理工具
"""

card_list = []  # 记录所有的名片字典


# 提供和名片相关的工具函数
def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)