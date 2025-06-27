class Books:
    def __init__(book, title, author, isbn):
        book.title = title
        book.author = author
        book.isbn = isbn
        book.is_checked_out = False


class Members:
    def __init__(member, name, member_id):
        member.name = name
        member.member_id = member_id
        member.borrowed_books = []


class Library:
    def __init__(library):
        library.members = []
        library.books = []

    def add_members(add_member, member):
        if any(m.member_id == member.member_id for m in add_member.members):
            print("This ID already exists, please create a new ID.")
        else:
            add_member.members.append(member)
            print(f"Member {member.name} with ID {member.member_id} has been successfully added.")
  
    def display_borrowed_books(borrowed_book, member_id):
        for member in borrowed_book.members:
            if member.member_id == member_id:
                if member.borrowed_books:
                    print(f"{member.name}'s borrowed books:")
                    for book in member.borrowed_books:
                        print(f"{book.title}")
                else:
                    print(f"{member.name}, you have not borrowed any books.")
                return
        print("Member not found.")

    def add_books(add_book, book):
        add_book.books.append(book)
        print(f"The book '{book.title}' by {book.author} has been successfully added.")
    
    def borrow_books(borrow_book, member_id, isbn):
        for member in borrow_book.members:
            if member.member_id == member_id:
                for book in borrow_book.books:
                    if book.isbn == isbn and book.is_checked_out == False:
                        book.is_checked_out = True
                        member.borrowed_books.append(book)
                        print(f"{member.name} borrowed {book.title} .")
                        return
        print("book not found or already borrowed")
                        
    def return_books(return_book, member_id, isbn):
        for member in return_book.members:
            if member.member_id == member_id:
                for book in member.borrowed_books:
                    if book.isbn == isbn:
                        if book.is_checked_out:
                            book.is_checked_out = False
                            member.borrowed_books.remove(book)
                            print(f"{member.name} returned '{book.title}'.")
                            return
                        else:
                            print(f"The book '{book.title}' is not currently borrowed.")
                        return
            print("Book not found in borrowed books.")
            return
    print("Member not found.")


library_files = Library()

book1 = Books("Hunger Games", "Suzanne Collins", "123")
book2 = Books("Maze Runner", "James Dashner", "145")
book3 = Books("Cyberpunk", "Someone", "432")
book4 = Books("Metal Gear Solid", "Hideo Kojima", "813")


member1 = Members("John", 1)
member2 = Members("Imane", 2)

library_files.add_members(member1)
library_files.add_members(member2)

library_files.add_books(book1)
library_files.add_books(book2)
library_files.add_books(book3)
library_files.add_books(book4)

library_files.borrow_books(1, "123")
library_files.borrow_books(2, "145")


while True:
    try:
        member_id = int(input("Please Enter Your ID: "))
        name = input("Please enter your name: ")
        
        found = False
        for member in library_files.members:
            if member.member_id == member_id:
                if member.name == name:
                    print(f"Welcome, {name}")
                    found = True
                    break
                else:
                    print("ID and name do not match.")
                    break
        
        if found:
            break
        
        create_account = input("Would you like to create an account? (yes/no): ")
        if create_account == "yes":
            while any(m.member_id == member_id for m in library_files.members):
                member_id = int(input("This ID already exists, please enter a new ID: "))
            new_member = Members(name, member_id)
            library_files.add_members(new_member)
            print(f"Welcome, {name}")
            break
        else:
            print("Please try again.")
    except ValueError:
        print("Please enter a valid ID.")

while True:
    choice = input(f"What would you like to do today, {name}?\n [1] View Borrowed Books\n [2] Add Book\n [3] Borrow Book\n [4] Return Book\n [5] Exit\n")
    if choice == "1":
        library_files.display_borrowed_books(member_id)
        continue
    if choice == "2":
        while True:
            book_title = input("Please write the name of the book you would like to add:")

            book_exists = any(b.title == book_title for b in library_files.books)
        
            if book_exists:
                print("This book already exists, please try again.")
            else:
                author = input("Please write the author of the book: ")
                isbn = input("Please write the ISBN of the book: ")
                new_book = Books(book_title, author, isbn)
                library_files.add_books(new_book)
                print(f"The book '{new_book.title}' by {new_book.author} has been successfully added.")
                break
        continue
    if choice == "3":
            isbn = input("Please enter the isbn of the book you want to borrow:")
            library_files.borrow_books(member_id, isbn)
            continue
    if choice == "4":
            isbn = input("Please enter the isbn of the book you want to return:")
            library_files.return_books(member_id, isbn)
            continue
    if choice == "5":
            print("Cya")
            break
    else:
            print("Invalid choice. Please try again.")





