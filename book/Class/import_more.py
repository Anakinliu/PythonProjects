from book.Class.electric_car import ElectricCar, Battery

my_e_car = ElectricCar("CHANGAN", "AAAAAA", "2018", "10000")
best = Battery(999999999)
my_e_car.battery = best
my_e_car.battery.describe_battery()
