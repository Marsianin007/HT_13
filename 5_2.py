# 5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).

books_list = []
bad_books_list = []
now_read_book_list = []
workers_list = []
users_list = []
library_list = []


class Library(object):
    def __init__(self, adress, lib_phone):
        self.adress = adress
        self.lib_phone = lib_phone
        library_list.append(self)


class Book(object):
    def __init__(self, book_name, book_author):
        self.book_name = book_name
        self.book_author = book_author


class User(object):
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number


class Bad_books(Book):
    def __init__(self, book_name, book_author, book_problem):
        super().__init__(book_name, book_author)
        self.book_problem = book_problem


class Student(User):
    def __init__(self, name, surname, phone_number, user_class):
        super().__init__(name, surname, phone_number)
        self.user_class = user_class

    def get_book(self, book_to_get, book_to_get_author):
        for i in books_list:
            if i.book_name == book_to_get and i.book_author == book_to_get_author:
                print("Вам видана книга")
                now_read_book_list.append(i)
                books_list.remove(i)
                return True

    def give_book(self, book_to_give, book_to_give_author):
        for i in now_read_book_list:
            if i.book_name == book_to_give and i.book_author == book_to_give_author:
                print("Дякую за повернення книги!")
                books_list.append(i)
                now_read_book_list.remove(i)
                return True

    def say_problem(self, book_name, book_author, book_problem):
        for i in now_read_book_list:
            if i.book_name == book_name and i.book_author == book_author:
                tmp = Bad_books(book_name, book_author, book_problem)
                bad_books_list.append(tmp)
                print("Дякую за повідомлення!")
                return True

    def look_all_lib(self):
        for i in library_list:
            print(f"Адреса: {i.adress}  Телефон: {i.lib_phone}")


class Worker(User):
    def __init__(self, name, surname, phone_number, experience):
        super().__init__(name, surname, phone_number)
        self.experience = experience

    def del_book(self, book_name, book_author):
        for i in books_list:
            if i.book_name == book_name and i.book_author == book_author:
                books_list.remove(i)
                print("Книга видалена")

    def add_book(self, book_to_add, book_to_add_author):
        check = True
        for i in books_list:
            if i.book_name == book_to_add and i.book_author == book_to_add_author:
                check = False
        if check:
            tmp = Book(book_to_add, book_to_add_author)
            books_list.append(tmp)
            print("Книга додана")
        else:
            print("Така книга вже є")

    def check_book(self, book_name_to_check, book_author_to_check):
        for i in books_list:
            if i.book_name == book_name_to_check and i.book_author == book_author_to_check:
                print("Книга знаходиться на балансі бібліотеки")
        for i in now_read_book_list:
            if i.book_name == book_name_to_check and i.book_author == book_author_to_check:
                print("Книга знаходиться у користуванні")
        for i in bad_books_list:
            if i.book_name == book_name_to_check and i.book_author == book_author_to_check:
                print("Книга знаходиться у списку проблемних книг")


def login_menu():
    global check
    phone, user_class, experience = "", 0, 0
    check = False
    user_name = input("Ваше ім'я: ")
    user_surname = input("Ваше прізвище: ")
    category = input("1. Учень \n2. Працівник  \nВиберіть категорію: ")
    if category == "1":
        for i in users_list:
            if i.name == user_name and i.surname == user_surname:
                check = True
                phone = i.phone_number
                user_class = i.user_class
        if check:
            print("Ласкаво просимо учню")
            start_menu_student(user_name, user_surname, phone, user_class)
        else:
            print("Перевірте данні або щоб зареєструватись натисніть '1'")
            num_to_do = input("Ваш вибір: ")
            if num_to_do == "1":
                name = input("Імя: ")
                surname = input("Прізвище: ")
                phone = input("Ваш телефон: ")
                user_class = input("Ваш клас: ")
                tmp = Student(name, surname, phone, user_class)
                users_list.append(tmp)
                print("Вхід")
                login_menu()
            else:
                login_menu()
    if category == "2":
        for i in workers_list:
            if i.name == user_name and i.surname == user_surname:
                phone = i.phone_number
                experience = i.experience
                check = True
    if check:
        print("Ласкаво просимо")
        start_menu_worker(user_name, user_surname, phone, experience)
    else:
        print("Перевірте данні або щоб зареєструватись натисніть '1'")
        num_to_do = input("Ваш вибір: ")
        if num_to_do == "1":
            name = input("Імя: ")
            surname = input("Прізвище: ")
            phone = input("Ваш телефон: ")
            experience = input("Ваш досвід: ")
            tmp = Worker(name, surname, phone, experience)
            workers_list.append(tmp)
            print("Вхід")
            login_menu()
        else:
            login_menu()


def start_menu_student(user_name, user_surname, phone, user_class):
    student = Student(user_name, user_surname, phone, user_class)
    print("Виберіть дію: \n1. Взяти книгу \n2. Віддати книгу \n3. Повідомити про проблему \n4. Подивитися всі бібліотеки")
    num = input("Ваш вибір: ")
    if not num.isdigit():
        print("Введіть число")
        start_menu_student(user_name, user_surname, phone, user_class)
    num = int(num)
    if num < 1 or num > 4:
        print("Невірний номер")
        start_menu_student(user_name, user_surname, phone, user_class)
    if num == 1:
        for i in books_list:
            print(f"Name: {i.book_name}  Author: {i.book_author}")
        book_to_get = input("Назва книги, яку бажаєте взяти: ")
        book_to_get_author = input("Автор цієї книги: ")
        if not student.get_book(book_to_get, book_to_get_author):
            print("Нажаль потрібної книги немає")

    if num == 2:
        book_to_give = input("Назва книги, яку бажаєте віддати ")
        book_to_give_author = input("Автор цієї книги: ")
        if not student.give_book(book_to_give, book_to_give_author):
            print("Такої книги немає на балансі школи")

    if num == 3:
        book_to_give = input("Назва книги, яка містить проблему: ")
        book_to_give_author = input("Автор цієї книги: ")
        book_to_give_problem = input("Яка проблема з книгою: ")
        if not student.say_problem(book_to_give, book_to_give_author, book_to_give_problem):
            print("Такої книги немає на балансі школи")

    if num == 4:
        student.look_all_lib()

    start_menu_student(user_name, user_surname, phone, user_class)


def start_menu_worker(user_name, user_surname, phone, experience):
    worker = Worker(user_name, user_surname, phone, experience)
    print("Виберіть дію: \n1. Видалити книгу \n2. Додати книгу \n3. Перевірити наявність")
    num = input("Ваш вибір: ")
    if not num.isdigit():
        print("Введіть число")
        start_menu_worker(user_name, user_surname, phone, experience)
    num = int(num)

    if num == 1:
        book_name_to_del = input("Назва книги, яку бажаєте видалити: ")
        book_author_to_del = input("Автор цієї книги: ")
        worker.del_book(book_name_to_del, book_author_to_del)

    if num == 2:
        book_to_add = input("Назва книги, яку бажаєте додати ")
        book_to_add_author = input("Автор цієї книги: ")
        worker.add_book(book_to_add, book_to_add_author)

    if num == 3:
        book_name_to_check = input("Назва книги, яку бажаєте перевірити: ")
        book_author_to_check = input("Автор цієї книги: ")
        worker.check_book(book_name_to_check, book_author_to_check)
    start_menu_worker(user_name, user_surname, phone, experience)


x = Book("Lala", "Dali")
y = Book("Python", "Ukr")
books_list.append(x)
books_list.append(y)


Vlad = Student("Vlad", "Vlad", "3456345", 9)
users_list.append(Vlad)
Anna = Worker("Anna", "Anna", "325236", 12)
workers_list.append(Anna)

this_lib = Library("Cherkassy, Shevhecnko 135", "0962876464")
center_lib = Library("Cherkassy, Mytnytsa 12", "09927655531")


login_menu()
