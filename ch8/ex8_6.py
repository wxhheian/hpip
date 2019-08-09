# import pizza   #导入整个pizza.py 即导入整个模块
#
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# from pizza import make_pizza #从模块中导入特定函数
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')

# from pizza import make_pizza as mp                 #使用as给函数指定别名
# mp(12,'mushrooms','green peppers','extra cheese')

# import pizza as p    #使用as给模块指定别名
# p.make_pizza(12,'mushrooms','green peppers','extra cheese')

from pizza import *             ##使用*号让Python导入模块中的所有函数
make_pizza(12,'mushrooms','green peppers','extra cheese')
