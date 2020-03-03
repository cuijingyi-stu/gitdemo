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


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 找到的名片
    """
    action_str = input("请选择要执行的操作" 
                       "[1]\\修改；[2]\\删除；[0]\\返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "修改姓名[不修改直接空格]：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "修改电话[不修改直接空格]：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "修改QQ[不修改直接空格]:")
        find_dict["email"] = input_card_info(find_dict["email"], "修改邮件[不修改直接空格]:")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)  # 删除名片


def input_card_info(dict_value, tip_message):
    """
     输入名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容；否则返回字典中原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)
    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3. 如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value


while True:

    # TODO(作者/邮件) 显示功能菜单
    show_menu()
    action_str = input("请选择希望的操作")  # 类型是字符串
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            new_card()
        # 显示全部
        elif action_str == "2":
            show_all()
        # 查询名片
        elif action_str == "3":
            search_card()
        pass  # 如果在开发程序时，不希望立刻编写分支内部的代码，可以使用 pass 关键字占位
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容，报错
    else:
        print("您输入的不正确，请重新选择")