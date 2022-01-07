# 5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
import datetime


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

        date_now = datetime.date.today()

        year = date_now.year + int(time_to_take)
        month = date_now.month
        day = date_now.day
        print(f"Чекаємо на Вас до {year}-{month}-{day} ")


x = Library()
x.look_all_books()
x.add_book()
x.search_book()
x.take_book()
