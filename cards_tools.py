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


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入email：")
    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    # 4.提示用户添加成功
    print("添加%s的名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在 名片数据 如果没有提示用户
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用【新增名片】功能")
    else:  # 或者在if下方（里面）写一个return关键字
        # 打印表头
        for biaotou in ["姓名", "电话", "QQ", "邮箱"]:
            print(biaotou, end="\t\t")
        print("")  # 在输出完“邮箱”后，还是希望换一行
        # 打印分割线
        print("=" * 50)
        # 遍历名片列表 一次输出字典信息
        for card_dict in card_list:
            # \t这种方法其实不太科学
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    # 2.遍历名片列表，搜索姓名；如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("==" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card(card_dict)
            # 为了防止函数太长，这个操作也用一个专门的函数来执行

            break  # 找到了就退出循环
    else:  # 遍历了名片列表后，没有找到
        print("抱歉，没有找打%s" % find_name)