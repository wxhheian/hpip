# for value in range(1,5):
#     print(value)
#
# numbers = list(range(1,6))
# print(numbers)
#
# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     # square = value**2
#     # squares.append(square）
#     squares.append(value**2)
#
# print(squares)


# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

#使用列表解析来生成列表
squares = [value**2 for value in range(1,11)]
print(squares)
