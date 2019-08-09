# user_0 = {
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
#     }
#
#
# for key, value in user_0.items():           #遍历时的返回顺序与存储顺序不一定相同
#     print("\nKey: " + key)
#     print("Value: " + value)


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

# for name,language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin,please take our poll")

for language in favorite_languages.values():             #遍历所有的值，没有考虑是否重复，为规避重复值，可以使用集合set
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())
