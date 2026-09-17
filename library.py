class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def displayinfo(self):
        print(f"TITLE : {self.title} \n AUTHOR : {self.author} \n AVAILABLE : {self.available}")
    
    def borrow(self):
        if self.available:
            self.available = False
            print("Book successfully borrowed")
            return True
        else:
            print("Book is not available")
            return False
    
    def return_book(self):
        if self.available is False:
            self.available = True
        else:
            print("Book was not borrowed")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
           self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
           book.return_book()
           self.borrowed_books.remove(book)
        else:
            print("Book was not borrowed")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        for book in self.books:
            book.displayinfo()

    def display_members(self):
        for member in self.members:
            print(member.name)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
               return book 

        print("Book not found")
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                print("Member found")
                return member
            
        print("member not found")
        return None

    def borrow_book(self, member, book):
        member.borrow_book(book)

    def return_book(self, member,book):
        member.return_book(book)

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Breaking Bad", "Joseph Mathew")

library = Library()

library.add_book(book1)
library.add_book(book2)

member1 = Member("Chirag")
library.add_member(member1)

while True:
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Display Members")
    print("5. Find Book")
    print("6. Find Member")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("Enter your choice:")

    if choice == "3":
       library.display_books()
    elif choice == "1":
         title = input("Enter Book Title:")
         author = input("Enter Author Name:")

         book = Book(title, author)
         library.add_book(book)
    elif choice == "2":
         name = input("Enter Member Name")
         member = Member(name)
         library.add_member(member)
    elif choice == "4":
         library.display_members()
    elif choice == "5":
        title = input("Enter Book Title:")
        library.find_book(title)
    elif choice == "6":
        name = input("Enter Member Name:")
        library.find_member(name)
    elif choice == "7":
        name = input("Enter Member Name:")
        member = library.find_member(name)
        
        title = input("Enter Book Title: ")
        book = library.find_book(title)

        if member and book:
            library.borrow_book(member, book)

    elif choice == "8":
        name = input("Enter Member Name")
        member = library.find_member(name)

        title = input("Enter Book Title")
        book = library.find_book(title)

        if member and book:
          library.return_book(member, book)
    elif choice == "9": 
         break
    else:
         print("Invalid choice")


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Breaking Bad", "Joseph Mathew")

library = Library()

library.add_book(book1)
library.add_book(book2)

member1 = Member("Chirag")
library.add_member(member1)