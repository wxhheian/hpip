name = "ada lovelace"
print(name.title())    #将每个单词的首字母改为大写，其他都是小写

name = "Ada lovelace"
print(name.upper())           #将字符串改为全部大写或全部小写
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print(full_name)

print("Hello," + full_name.title() + "!")
message = "Hello," + full_name.title() + "!"
print(message)
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python  '
print(favorite_language)
print(favorite_language.rstrip())    #string.rstrip() 删除右端的空白    string.lstrip()删除左端的空白   string.strip()删除两端的空白
print(favorite_language)           #并非永久删除空白
favorite_language = favorite_language.rstrip()
print(favorite_language)

#message = 'One of Python's strngths is its diverse community'     #报错 invalid syntax
  
