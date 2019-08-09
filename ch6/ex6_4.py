#字典列表
# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 = {'color':'red','points':15}
#
# aliens = [alien_0,alien_1,alien_2]
#
# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_number in range(30):      #创建30个绿色的外星人
#     new_alien = {'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)

#显示前5个外星人
# for alien in aliens[:5]:
#     print(alien)
# print('...')
#
# print("Total number of aliens: " + str(len(aliens)))

# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# for alien in aliens[0:5]:
#     print(alien)
# print('...')


#列表字典
# pizza = {
#     'crust':'thick',
#     'toppings':['mushrooms','extra cheese'],
#     }
#
# print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following topping:")
#
# for topping in pizza['toppings']:
#     print("\t" + topping)


#在字典中嵌套字典
users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },

    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }

for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())
