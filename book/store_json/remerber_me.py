import json


def get_user():
    """
    得到用户名
    :return:
    """
    file_name = "numbers.json"
    try:
        # 已有文件则载入用户
        with open(file_name) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """
    问候用户, 打印出用户名
    :return:
    """
    user_name = get_user()
    if user_name:
        print("welcome, " + user_name + " !")
    else:
        # 如果没有json文件则创建并保存输入用户
        username = input("what's your name? \n input here: ")
        file_name = "numbers.json"
        with open(file_name, 'w') as file_obj:
            json.dumps(username, file_obj)
            print("we'll remember you when you come back, " + username + "!")


    # try:
    #     # 已有文件则载入用户
    #     with open(file_name) as file_obj:
    #         username = json.load(file_obj)
    # except FileNotFoundError:
    #     # 如果没有json文件则创建并保存输入用户
    #     username = input("what's your name?")
    #     with open(file_name, 'w') as file_obj:
    #         json.dumps(username, file_obj)
    #         print("we'll remember you when you come back, " + username + "!")
    # else:
    #     # 已有文件, 无异常
    #     print("welcome, " + username + " !")


greet_user()
