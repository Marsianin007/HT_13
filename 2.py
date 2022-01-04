# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
# які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name,
# show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

class Person(object):

    def __init__(self, *args):
        if len(args) >= 2:
            self.age = args[0]
            self.name = args[1]
        self.another = []
        for i in args:
            self.another.append(i)

    def show_age(self):
        print(f"Age: {self.age}")

    def print_name(self):
        print(f"Name: {self.name}")

    def show_all_information(self):
        print(f"Age: {self.age}")
        print(f"Name: {self.name}")
        for i in self.another:
            print(i)


first_exem = Person(18, "Vlad", "fdsgsdfg", "gdfsgdsf", "sdfhdsfh")

first_exem.show_age()
first_exem.print_name()
first_exem.show_all_information()

first_exem.profession = "Builder"

second_exem = Person()
second_exem.profession = "Driver"

print(first_exem.profession, second_exem.profession)