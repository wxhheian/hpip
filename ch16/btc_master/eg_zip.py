# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

from itertools import groupby

x_data = [1,1,2,3,3,4,4,5]
y_data = [4,5,6,5,7,7,8,9]

xy_map = []
for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _:_[0]):
    y_list = [v for _,v in y]
    xy_map.append([x,sum(y_list)/len(y_list)])

print(xy_map)
x_unique,y_mean = [*zip(*xy_map)]
