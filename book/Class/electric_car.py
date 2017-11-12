from book.Class.car import Car


class Battery:

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""

        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("this car has a " + str(self.battery_size) + "-kwh battery!")


class ElectricCar(Car):
    """
    电动汽车的特殊功能
    """

    def __init__(self, make, model, year, battery_size):
        """
        初始化父类属性
        :param make:
        :param model:
        :param year:
        :param battery_size:
        """
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

    # 由Battery类管理!
    # def describe_battery(self):
    #     print("this car has " + str(self.battery_size) + " -kwh battery")

    def get_descriptive(self):
        """重写父类方法"""
        print("我是电瓶车!")


# my_electric_car = ElectricCar('tesla', 'no model', 2017, 555)
# my_electric_car.get_descriptive()
# my_electric_car.battery.describe_battery()
