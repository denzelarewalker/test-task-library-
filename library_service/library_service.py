import json


class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def __str__(self) -> str:
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"
    



class Library:
    def __init__(self, basefile_path: str):
        self.basefile_path = basefile_path
        self.books = self.load_books() 


    def load_books(self) -> list[Book]:
        try:
            with open(self.basefile_path, "r") as f:
                data = json.load(f)
                books_list = []
                for book_data in data:
                    book = Book(*book_data.values())
                    books_list.append(book)
            return books_list
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def save_books(self, books: list[Book]):
        book_data = [vars(book) for book in books] 
        with open(self.basefile_path, "w") as f:
            json.dump(book_data, f, indent=4)
    

    def generate_id(self) -> int:
        return max(book.id for book in self.books) + 1 if self.books else 1

    

    def add_book(self, title: str, author: str, year: int):
        book = Book(self.generate_id(), title, author, year)
        self.books.append(book)
        self.save_books(self.books)
        print(f"Book '{title}' added")


    def delete_book(self, book_id: int):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Invalid book ID")
            return
        
        book_found = False
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                book_found = True
                break

        if not book_found:
            print(f"Book with ID {book_id} not found")
            return
        
        self.save_books(self.books)
        print(f"Book with ID {book_id} deleted")

    
    def search_book(self, search_term: str|int):
        results = [book for book in self.books if search_term.lower() in book.title.lower() or \
                                                search_term.lower() in book.author.lower() or \
                                                search_term == int(book.year)]
        if results:
            for book in results:
                print(book)
            return results
        else:
            print('There are no books on request')


    def all_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("The library is empty")


    def change_book_status(self, book_id: int, new_status: str):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Invalid book ID")
            return

        valid_statuses = ["в наличии", "выдана"]
        if new_status not in valid_statuses:
            print("Invalid status. Acceptable statuses: 'в наличии', 'выдана'")
            return

        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books(self.books)
                print(f"The status of a book with ID {book_id} has been changed to '{new_status}'")
                return
        print(f"Book with ID {book_id} not found")



