class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0            #设置默认属性，就不需要提供形参了

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self,mileage):
        """通过方法修改属性的值，
        禁止将里程表往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading += miles

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23    #直接修改默认属性的值
my_new_car.update_odometer(24)           #通过方法修改属性的值
my_new_car.read_odometer()
my_new_car.update_odometer(21)
my_new_car.increment_odometer(3)
my_new_car.read_odometer()
