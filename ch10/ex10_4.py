# import json
#
# numbers = [2,3,5,7,11,13]
#
# filename = 'numbers.json'
# with open(filename,'w') as f_obj:
#     json.dump(numbers,f_obj)


# import json
#
# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
#
# print(numbers)


# import json
#
# username = input("What is your name?")
#
# filename = 'username.json'
# with open(filename,'w') as f_obj:
#     json.dump(username,f_obj)
#     print("We'll remember you when you come back, " + username + "! ")
#


# import json
#
# filename = 'username.json'
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + " !")



# import json
# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name?")
#     with open(filename,'w') as f_obj:
#         json.dump(username,f_obj)
#         print("We'll remember you when you come back," + username + " !")
# else:
#     print("Welcome back, " + username + "! ")



##对40——51行进行重构
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_user_name():
    """"提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back," + username + "！")
    else:
        username = get_user_name()
        print("I'll remember you when you come back," + username + '!')

greet_user()
