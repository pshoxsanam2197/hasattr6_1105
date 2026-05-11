class Simple:
    def info_jon(self):
        print(f"Simple info")

class MyClass:
    def __init__(self,x, y):
        self.__x = x
        self.__y = y

    def method_1(self, obj):
        if hasattr(obj, "info"):
            obj.info()
        else:
            print("Bu method da info method yo'q")

obj = MyClass(40, 30)

s = Simple()
obj.method_1(s)

class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")


class Simple:
    def test(self):
        print("Oddiy method")





# 1-m
class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")


class Simple:
    def test(self):
        print("Oddiy method")

class Profile:
    def check_profile(self, obj):
        if hasattr(obj, "show_info"):
            obj.show_info()
        else:
            print("show_info method topilmadi")

p1 = Person("Azamat", 21)
s1 = Simple()

profile = Profile()

profile.check_profile(p1)
print("----------")
profile.check_profile(s1)



# 2-m
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start_engine(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")

class Simple:
    def test(self):
        print("Oddiy method")

class Driver:
    def drive(self, car_obj):
        if hasattr(car_obj, "start_engine"):
            car_obj.start_engine
        else:
            print("start_engine topilmadi")

c1 = Car("BMW", 220)
s1 = Simple

driver = Driver()

driver.drive(c1)
print("--------------")
driver.drive(s1)



# 3-m
class Book:
    def __init__(self, title, auther):
        self.title = title
        self.auther = auther

    def read(self, page):
        print(f"Sahifa: {page}")

class Notebook:
    def write(self, text):
        print(f"Text: {text}")

class Library:
    def open_book(self, obj, page):
        if hasattr(obj, "read"):
            obj.read(page)
        else:
            print(f"read methodi topilmadi")

b1 = Book('Binafsha shulasi', 'Usoma Muslim' )
n1 = Notebook()

library = Library()

library.open_book(b1, 4)
print("----")
library.open_book(n1,8)



# 4-m
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self, sound):
        print(f"Sound: {sound}")

class Toy:
    def play(self):
        print("Oddiy method")

class Zo:
    def test_sound(self, animal, sound):
        if hasattr(animal, "sound"):
            animal.sound()
        else:
            print("sound method topilmadi.")

a1 = Animal("Cat", "Black")
t1 = Toy()

zo = Zo()
zo.test_sound(a1, "miav")
a1.make_sound("miav")
zo.test_sound(a1, "miav")
