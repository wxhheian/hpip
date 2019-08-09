# with open('pi_digits.txt') as file_object:            #with...as...  用于打开和关闭文件
#     contents = file_object.read()                #读取整个文件
#     print(contents.rstrip())

#文件相对路径:text_files在当前程序所在路径
# with open('text_files/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

#绝对路径
# with open('/home/wxhheian/hpip/ch10/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

##逐行读取
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#读取每一行，并将其存储在一个列表中
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# print(lines)          #以列表形式展示
# for line in lines:
#     print(line.rstrip())

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))


filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(pi_string[:52] + '...')
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print('Yes')
else:
    print('No')
