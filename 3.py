# 3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням
# white і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять
# методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

class Figure(object):
    color = "White"

    def change_color(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, length, hight):
        self.length = length
        self.hight = hight


class Square(Figure):
    def __init__(self, len_of_side):
        self.len_of_side = len_of_side


x = Figure()
print(x.color)
x.change_color("Blue")
print(x.color)

oval_1 = Oval(15, 13)
square_1 = Square(12)

print(f"Len of oval: {oval_1.length}")
print(f"Hight of oval: {oval_1.hight}")
print(f"Len of square side: {square_1.len_of_side}")