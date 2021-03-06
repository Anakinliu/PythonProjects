class Restaurant:
    """
    餐馆
    """

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe(self):
        print("name: " + self.name + ", type: " + self.cuisine_type)

    def open(self):
        print("opening!")

    def set_number_served(self, served):
        if served > 0:
            self.number_served = served

    def increment_number_served(self, served):
        if served > 0:
            self.number_served += served


my_restaurant = Restaurant("gggg", "KFC")
my_restaurant.set_number_served(100)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)
print("==================")
print(my_restaurant.__class__)
print(Restaurant.__class__)  # 类定义就是type类的一个对象的类型声明, 基类为object
x = Restaurant.__class__
print(x.__bases__)
