# 6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Example_class(object):
    count = 0

    def __init__(self):
        Example_class.count += 1


x_1 = Example_class()
x_2 = Example_class()
x_3 = Example_class()


print(Example_class.count)