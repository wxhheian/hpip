"""一个可以用于表示燃油汽车和电动汽车的类"""

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

    def fill_gas_tank(self):
        """汽车或许存在输油的问题"""
        print("Car need a gas tank!")


class Battery():
    """一次模拟电动汽车电瓶的简单测试"""

    def __init__(self,battery_size=70):
        """初始化电瓶的属性，如果没有为battery_size提供值，它将默认为70"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处
    初始化父类属性，再初始化电动汽车特有的属性"""

    def __init__(self,make,model,year):
        """初始化父类属性"""
        super().__init__(make,model,year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def fill_gas_tank(self):                   #在子类中写一个与父类中命名一样的方法，则只会关注子类的方法
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank！")
