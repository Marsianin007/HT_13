# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати
# математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
#   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )

class Calc(object):
    """Клас для виконання математичних операцій, для використання треба викликати методи minus(), plus(), """ \
    """miltiply(), divide_up() та передати у якості аргументів перше та друге число """

    last_result = None

    def minus(self, first, second):
        self.last_result = first - second
        print(self.last_result)

    def plus(self, first, second):
        self.last_result = first + second
        print(self.last_result)

    def multiply(self, first, second):
        self.last_result = first * second
        print(self.last_result)

    def divide_up(self, first, second):
        if second != 0:
            self.last_result = first / second
            print(self.last_result)
        else:
            print("Поділити на нуль неможливо")


calculate = Calc()
calculate.plus(5, 7)
calculate.minus(5, 9)
calculate.multiply(7, 9)
calculate.divide_up(8, 5)

print(Calc.last_result)
print(Calc.__doc__)