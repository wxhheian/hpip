# cars = ['audi','bmw','subaru','toyata']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
# car = 'Audi'
# print(car == 'audi')
#
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')


#and  or

#检查特定值是否在列表中
requested_toppings = ['mushrooms','onions','pipeapple']
print('mushrooms' in requested_toppings)

#检查特定值是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
