# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
# usernames = ['hannah','ty','margot']
# greet_users(usernames)

#需要打印的设计存储在一个列表中，打印后移交到另一个列表
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


#定义函数完成上述过程
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []


# print_models(unprinted_designs,completed_models)             #传递unprinted_designs本身，对unprinted_designs作出修改
# show_completed_models(completed_models)

print_models(unprinted_designs[:],completed_models)             #传递unprinted_designs副本，对unprinted_designs不作出修改
show_completed_models(completed_models)
