# players = ['charles','martina','michael','florence','eli']
# print(players[0:3])
# print(players[:4])             #从头开始，直到索引4
# print(players[2:])
# print(players[-3:])            #负数索引返回离列表末尾相应距离的元素

# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]                 #创建列my_food的副本，然后将这个副本存储到变量friend_foods中
# print(my_foods)
# print(friend_foods)
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print(my_foods)
# print(friend_foods)



my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods             #简单地将my_foods赋给friend_foods,不能得到两个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)                                      ##区别11—18行代码的区别
print(friend_foods)
