# cars = ['bmw','audi','toyota','subaru']
# cars.sort()               #sort() 区分大小写，且对list顺序进行了永久性修改
# print(cars)

# cars = ['bmw','audi','toyota','subaru']
# cars.sort(reverse=True)              #按相反顺序
# print(cars)

# cars = ['bmw','audi','toyota','subaru']
# print("Here is the original list:")
# print(cars)
#
# print("\nHere is the sorted list:")
# print(sorted(cars))                     #sorted() 保留list原来的排列顺序，同时以特定的顺序展现它们
#
# print("\nHere is the original list again:")
# print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.reverse()           #反转list的排序
print(cars)
print(len(cars))
