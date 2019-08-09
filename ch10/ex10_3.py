# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them:")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("Second number:")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can' divide by 0!")
#     else:
#         print(answer)





def count_words(filename):
    """计算一个文件有多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = 'Sorry, the file ' + filename + "does not exist."
        # print(msg)
        pass
    else:
        #计算有多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','siddartha.txt','moby_dict.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
