# 4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури
#  при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.


class Figure(object):
    def __init__(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, color, length, hight):
        self.color = color
        self.length = length
        self.hight = hight


class Square(Figure):
    def __init__(self, color, len_of_side):
        self.color = color
        self.len_of_side = len_of_side


x = Figure("Blue")
print(x.color)


oval_1 = Oval("Red", 15, 13)
square_1 = Square("Black", 12)

print(f"Len of oval: {oval_1.length}")
print(f"Hight of oval: {oval_1.hight}")
print(f"Len of square side: {square_1.len_of_side}")
print(f"Oval color: {oval_1.color}")
print(f"Square color: {square_1.color}")