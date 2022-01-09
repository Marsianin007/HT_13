# 5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
import datetime

math_list, physics_list, english_list = [], [], []
takes_books = []

class Books(object):
    def __init__(self, book_name, book_author):
        self.book_name = book_name
        self.book_author = book_author


class Books_for_students(Books):
    def __init__(self, book_name, book_author, subject, school_class):
        super().__init__(book_name, book_author)
        self.subject = subject
        self.school_class = school_class
        tmp_list = [book_name, book_author, subject, school_class]
        if subject == "Математика": math_list.append(tmp_list)
        if subject == "Фізика": physics_list.append(tmp_list)
        if subject == "English": english_list.append(tmp_list)

class Books_for_teachers(Books):
    def __init__(self,  book_name, book_author, subject, school_class, book_type):
        super().__init__(book_name, book_author)
        self.subject = subject
        self.school_class = school_class
        self.book_type = book_type
        tmp_list = [book_name, book_author, subject, school_class, book_type]
        if subject == "Математика": math_list.append(tmp_list)
        if subject == "Фізика": physics_list.append(tmp_list)
        if subject == "English": english_list.append(tmp_list)


def start_menu():
    global check
    print("Добрий день, виберіть Вашу категорію: \n1.Учень \n2.Вчитель")
    user_category = input("Ваша категорія: ")
    if not user_category.isdigit():
        print("Введіть будь ласка цифру")
        start_menu()
    user_category = int(user_category)
    if user_category < 1 or user_category > 2:
        print("Такої відповіді не існує")
        start_menu()

    if user_category == 1:
        print("Введіть, який предмет вас цікавить")
        print("1. Математика \n2. Фізика \n3. English")
        subj = input("Ваш вибір: ")
        if not subj.isdigit():
            print("Введіть число")
            start_menu()
        subj = int(subj)
        if subj < 1 or subj > 3:
            print("Такої відповіді не існує")
            start_menu()
        books_names_list = []
        if subj == 1:
            for i in math_list:
                books_names_list.append(i[0])
        if subj == 2:
            for i in physics_list:
                books_names_list.append(i[0])
        if subj == 3:
            for i in english_list:
                books_names_list.append(i[0])
        book_to_take = input("Введіть назву книги, яку хочете взяти: ")
        if book_to_take not in books_names_list:
            print("Невірна назва або книги не існує")
            start_menu()
        user_class = input("Введіть Ваш клас будь ласка: ")
        if not user_class.isdigit():
            print("Введіть число!")
            start_menu()
        user_class = int(user_class)
        if user_class < 1 or user_class > 11:
            print("Такого класу не існує")
            start_menu()
        check = False
        if subj == 1:
            for i in math_list:
                if book_to_take in i and user_class in i and len(i) != 5:
                    check = True
        if subj == 2:
            for i in physics_list:
                if book_to_take in i and user_class in i and len(i) != 5:
                    check = True
        if subj == 3:
            for i in english_list:
                if book_to_take in i and user_class in i and len(i) != 5:
                    check = True
        if check:
            user_name = input("Введіть Ваше прізвище та ім'я: ")
            date_now = datetime.date.today()
            year = date_now.year + 3
            month = date_now.month
            day = date_now.day
            date_str = f"{year - 1}-{month}-{day}"
            user_list = [user_name, book_to_take, date_str]
            takes_books.append(user_list)
            print(f"Дякую, Вам видана книжка до {year}-{month}-{day}")
            take_list = [user_name, book_to_take, date_now]
            takes_books.append(take_list)
        else:
            print("Для вашого класа в наявності немає потрібної книги...")
            start_menu()





    check = False
    if user_category == 2:
        print("Введіть, який предмет вас цікавить")
        print("1. Математика \n2. Фізика \n3. English")
        subj = input("Ваш вибір: ")
        if not subj.isdigit():
            print("Введіть число")
            start_menu()
        subj = int(subj)
        if subj < 1 or subj > 3:
            print("Такої відповіді не існує")
            start_menu()
        books_names_list = []
        if subj == 1:
            for i in math_list:
                books_names_list.append(i[0])
        if subj == 2:
            for i in physics_list:
                books_names_list.append(i[0])
        if subj == 3:
            for i in english_list:
                books_names_list.append(i[0])
        book_to_take = input("Введіть назву книги, яку хочете взяти: ")
        if book_to_take not in books_names_list:
            print("Невірна назва або книги не існує")
            start_menu()

        user_class = input("Введіть потрібний клас будь ласка: ")
        if not user_class.isdigit():
            print("Введіть число!")
            start_menu()
        user_class = int(user_class)
        if user_class < 1 or user_class > 11:
            print("Такого класу не існує")
            start_menu()
        if subj == 1:
            for i in math_list:
                if book_to_take in i and i[3] == user_class and len(i) == 5:
                    check = True
        if subj == 2:
            for i in physics_list:
                if book_to_take in i and i[3] == user_class and len(i) == 5:
                    check = True
        if subj == 3:
            for i in english_list:
                if book_to_take in i and i[3] == user_class and len(i) == 5:
                    check = True
        if check:
            book_type = ""
            if subj == 1:
                for i in math_list:
                    if book_to_take in i:book_type = i[4]
            if subj == 2:
                for i in physics_list:
                    if book_to_take in i:book_type = i[4]
            if subj == 3:
                for i in english_list:
                    if book_to_take in i:book_type = i[4]
            user_name = input("Введіть Ваше прізвище та ім'я: ")
            date_now = datetime.date.today()
            year = date_now.year + 1
            month = date_now.month
            day = date_now.day
            date_str = f"{year - 1}-{month}-{day}"
            user_list = [user_name, book_to_take, date_str, "teacher"]
            takes_books.append(user_list)
            print(f"Ваша книга: {book_to_take}, тип: {book_type} до {year}-{month}-{day}")
        else:
            print("Такої книги немає в наявності")
            start_menu()

x = Books_for_students("Початкова фізика", "Іванов", "Фізика", 7)
y = Books_for_teachers("Вища математика", "Мерзляк", "Математика", 11, "Робочий зошит")
z = Books_for_students("English B1", "Меркель", "English", 10)

start_menu()
print(takes_books)