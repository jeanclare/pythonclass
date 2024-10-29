#parent class
#managing a Library system
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
            return f"The Title is {self.title}, Author is {self.author}, Year is {self.year} and Year of publication is {self.year}"

#child class/derived class

class LibraryBook(Book):
    def __init__(self, title, author, year,isbn,copies_available):
        super().__init__(title, author, year)
        self.isbn = isbn
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"No of copies available: {self.title} unavailable"
    def return_book(self):
            self.copies_available += 1
            return f"{self.title} returned. Copies left: {self.copies_available}"

#usage example
book1 = LibraryBook("Confessions of Nairobi Women", "Joan Thatiah", 2020, "1254-5577", 20)
print(book1.display_info())


print(book1.borrow_book())
print(book1.return_book())
