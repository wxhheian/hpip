# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles.insert(0,'ducati')   #在索引0处插入元素‘ducati’
# print(motorcycles)
# motorcycles.insert(1,'ducati')
# print(motorcycles)


# del motorcycles[0]
# print(motorcycles)

# poped_motorcycle = motorcycles.pop(2)    #pop()默认弹出最后一个  pop(2)弹出第3个
# print(motorcycles)
# print(poped_motorcycle)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')              #根据具体的值删除  remove只删除第一个指定的值，如果有多个‘ducati’,需要要循环来删除
print(motorcycles)
