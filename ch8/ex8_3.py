# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# musician = get_formatted_name('jimi','hendrix')
# print(musician)


# def get_formatted_name(first_name,middle_name,last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
#
# musician = get_formatted_name('john','lee','hooker')
# print(musician)


# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# musician1 = get_formatted_name('john','lee','hooker')
# print(musician1)
# musician2 = get_formatted_name('jimi','hendrix')
# print(musician2)


#函数可以返回任何类型的值
# def build_person(first_name,last_name,age=''):
#     """返回一个字典，其中包含一个人的信息"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician1 = build_person('jimi','hendrix')
# print(musician1)
# musician2 = build_person('jimi','hendrix',27)
# print(musician2)


def get_formatted_name(first_name,last_name):
    """返回一个字典，其中包含一个人的信息"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")
