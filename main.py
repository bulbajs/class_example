# class Person:
#
#     def __init__(self, name, age):  # name, age - атрибуты
#         self.name = name  # имя человека
#         self.age = age  # возраст человека
#
#
# tom = Person("Tom", 22)  # tom - имя объекта, "Tom" и 22 - атрибуты
# adel = Person("Адея", 3)
# tom.age = 5
# tom.name = "Атьём"
# # обращение к атрибутам
# # # получение значений
# tom.company = "Яндекс" # Можно добавлять атрибуты вне класса, но могут быть ошибки
# print('Его зовут', tom.name, 'и ему', tom.age, 'годиков.')  # Tom
# print ('Он сина юбит одну девочку по имени',adel.name,',которой', adel.age, 'годика.')
# print(tom.company)

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name  # имя человека
#         self.age = age  # возраст человека
#
#     def display_info(self):
#         print(f"Имя: {self.name}  а  возраст :{self.age} годиков")
#
#
# tom = Person("Tom", 22)
# tom.display_info()  # Name: Tom  Age: 22
#
# bob = Person("Bob", 43)
# bob.display_info()  # Name: Bob  Age: 43


# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
#
#     def __del__(self):
#         print("Удален человек с именем", self.name)
#
#
# def create_person():
#     tom = Person("Tom")
#
#
# create_person()

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2*(self.length+self.width)


val = Rectangle(4,5)
val.width = 5
# print(f'Периметр = {P}, а площадь = {S}, хватит ныть, займись делом')
print(f'Площадь = {val.area()} Периметр = {val.perimeter()}')


