import json

file_name = "numbers.json"
try:
    # 已有文件则载入用户
    with open(file_name) as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    # 如果没有json文件则创建并保存输入用户
    username = input("what's your name?")
    with open(file_name, 'w') as file_obj:
        json.dumps(username, file_obj)
        print("we'll remember you when you come back, " + username + "!")
else:
    # 已有文件, 无异常
    print("welcome, " + username + " !")