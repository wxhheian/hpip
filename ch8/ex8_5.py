# def make_pizza(*toppings):           # *toppings创建一个空个元组，并将收到的所有值封装到这个元组中
#     """打印顾客点的所有配料"""
#     print(toppings)
#
# make_pizza('peperoni')
# make_pizza('mushrooms','green peppers','extra cheese')
#Result:
# ('peperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     """概述要制作的pizza"""
#     print("\nMaking a pizza with the following toppings")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

# def make_pizza(size,*toppings):
#     print("\nMaking a " + str(size) +
#            "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza(16,'pepperoni')
# make_pizza(32,'mushrooms','green peppers','extra cheese')


#使用任意数量的关键字实参
def build_profile(first,last,**user_info):               #形参**user_info中的两个*号让python创建一个名为user_info的空字典，并将收到的键-值对都封装在这个字典里
    """创建一个字典，其中包含我们知道的有关用户的一切
    我们总是从用户那里受到两项信息：姓和名。遍历字典user_info中的键-值对，并将每个键-值对都加到字典profile中"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    #print(user_info)
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
                             location='princton',          #注意这里location不用加'' 
                             field='physics')
print(user_profile)
