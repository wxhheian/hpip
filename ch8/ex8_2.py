# def describe_pet(animal_type,pet_name):
#     """显示宠物 的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet('hamster','harry')             #实参的顺序很重要

# def describe_pet(animal_type,pet_name):
#      """显示宠物 的信息"""
#      print("\nI have a " + animal_type + ".")
#      print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type='hamster',pet_name='harry')            #关键字实参，顺序不重要
# describe_pet(pet_name='harry',animal_type='hamster')              #与13行效果相同


def describe_pet(pet_name,animal_type='dog'):                 #形参指定默认值，形参的默认值应该放在最后
    """显示宠物 的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(pet_name='while')
# describe_pet('while')
# describe_pet(pet_name='harry',animal_type='hamster')   #若显式地给animal_type提供实参，则形参的默认值可以忽略
describe_pet('harry','hamster')           #若显式地给animal_type提供实参，则形参的默认值可以忽略
