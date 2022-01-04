# 5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).

from datetime import date


class Library(object):

    list_of_books = ["Буквар", "Пітон для чайників", "10050 спроб написати код з першого разу"]

    def add_book(self):
        book = input("Введіть назву книжки, яку хочете додати: ")
        self.list_of_books.append(book)

    def look_all_books(self):
        for i in self.list_of_books:
            print(f"Book: {i}")

    def search_book(self):
        book_to_find = input("Введіть назву книжку, котру хочете знайти:")
        book_to_find = book_to_find.replace(" ", "")
        if book_to_find in self.list_of_books:
            print("Така книжка присутня")
        else:
            print("Нажаль біблітотека не містить такої книжки")

    def take_book(self):
        book = input("Введіть назву книжку, котру хочете взяти:")
        book = book.replace(" ", "")
        if book not in self.list_of_books:
            print("Такої книжки немає")
            raise SystemExit
        time_to_take = input("Введіть на яку кількість років хочете взяти книжку(максимум 3 роки): ")
        if not time_to_take.isdigit():
            print("Введіть число!")
            raise SystemExit

        if int(time_to_take) > 3:
            print("Максимум 3 роки!")
            raise SystemExit

        date_now = str(date.today())
        year = int(date_now[0:4]) + int(time_to_take)
        month = int(date_now[5:7])
        day = int(date_now[8:10])
        print(f"Чекаємо на Вас до {year}-{month}-{day} ")


x = Library()
x.add_book()
x.look_all_books()
x.search_book()
x.take_book()