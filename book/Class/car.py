class Car:
    """模拟汽车"""

    def update_odometer(self, mileage):
        """
        禁止回拨里程表!
        :param mileage:
        :return:
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def update_year(self, year):
        self.year = year

    def __init__(self):
        """初始化汽车的属性"""
        self.make = 2
        self.model = 3
        self.year = 3
        # 属性可以不由参数传递, 可以指定有默认值的属性
        self.odometer_reading = 0

    def get_descriptive(self):
        """返回值存储到str, 并返回整洁的描述型信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("this car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4')
print(my_new_car.get_descriptive())
my_new_car.read_odometer()
my_new_car.year = 2018
print(my_new_car.get_descriptive())
my_new_car.update_year(2020)
print(my_new_car.get_descriptive())


class ElectricCar(Car):
    """
    电动汽车的特殊功能
    """

    def __init__(self, make, model, year):
        """
        初始化父类属性
        :param make:
        :param model:
        :param year:
        """
        super().__init__()


my_electric_car = ElectricCar('tesla', 'no model', 2017)
print(my_electric_car.get_descriptive())
