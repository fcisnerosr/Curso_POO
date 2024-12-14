class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.avaiable = True

    def borrow(self):
        if self.avaiable:
            self.avaiable = False
            print(f'El libro {self.title} ha sido prestado')
        else:
            print(f'El libro {self.title} no está diposnible')

        def return_book(self):
            self.aviable = True
            print(f'El libro {self.title} ha sido devuelto')

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.name= user_id
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.avaiable:
            book.borrow()
            self.borrowed_book.append(book)
        else:
            print(f'El libro {book.title} no está disponible')

    def return_book(self,book):
        if book is self.borrowed_books:
            book.return_book()
            self.borrowed_books .remove(book)
        else:
            print(f'El libro {book.title} no está en la lista de prestados')

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado')

    def add_users(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido registrado')

    def show_avaiable_books(self):
        print('Los libros disponibles:')
        for book in self.books:
            if book.avaiable:
                print(f'{book.title} por {book.author}')

book1 = Book('El principito', 'Antoine de Saint')
book2 = Book('1984', 'George Orwell')
User1 = User('Carli', '001')
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_users(User1)
