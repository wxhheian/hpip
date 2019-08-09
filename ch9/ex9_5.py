from collections import OrderedDict      #在模块中导入类

favorite_languages = OrderedDict()      #初始化实例，创建一个空的有序字典

favorite_languages['jen'] ='python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " +
          language.title() + ".")
