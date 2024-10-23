from abc import ABC, abstractmethod

class Laptop(ABC):
    def __init__(self, brand, make, storage, speed):
        self.brand = brand
        self.make = make
        self.storage = storage
        self.speed = speed
    @abstractmethod
    def print_name(self):
        return f"This is {self.brand} {self.make}"

    def get_speed(self, speed):
        return f"This is {self.brand} {self.make} --{self.speed} {speed}"
class RefurbishedLaptop(Laptop):
    def print_name(self):
        pass

    def __init__(self, brand, make, storage, speed, color, os, core_no):
        super().__init__(self, brand, make, storage)
        self.color = color
        self.os = os
        self.core_no = core_no

    def print_laptop(self):
        return f"This is a {self.color},{self.brand},{self.make},{self.storage},{self.speed},{self.os},{self.core_no}"
    def get_speed(self, speed):
        return f"{self.speed} {speed}"


laptop1 = RefurbishedLaptop("hp", "yoga", "256ssd", "3.5", "Black", "corei7", "4")
laptop2 = RefurbishedLaptop("lenovo", "x260", "500", "4.0", "Silver", "corei7", "8")


print(laptop1.print_name())
laptop2.print_name()
laptop1.get_speed("Ghz")
laptop2.get_speed("Ghz")
print(laptop1.print_laptop())
# print(laptop2.get_speed(2.4))


