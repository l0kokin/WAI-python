from random import randint

# constant. just a convention to not change this
CURRENT_YEAR = 2024

class Book:
    # constructor function. self is this keyword
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # standard method
    def get_age(self):
        return CURRENT_YEAR - self.year

    # self ხდება ის ობიექტი რაც შექმენი და არა თვითონ კლასი
    @classmethod
    def get_random_book(cls):
        book = cls(f"book_{randint(1,10)}", f"author_{randint(1,10)}", randint(0, 2024))
        return book

    # ეუბნები რო არაფერი არ დასეტოს ჯერ
    @staticmethod
    def get_classic(book):
        # if (book.year > 1950):
        #     return False
        # return True
        # or
        # return True if book.year < 1950 else False
        # or
        return book.year < 1950

    # dunder
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year}"

book_random = Book.get_random_book()
print(book_random)