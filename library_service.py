import json


class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def __str__(self) -> str:
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"
    



class Library:
    def __init__(self, basefile_path: str):
        self.basefile_path = basefile_path
        self.books = self.load_books() 


    def load_books(self) -> list[Book]:
        """Loads data from a JSON file"""
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
        """Saves books to a JSON file"""
        book_data = [vars(book) for book in books] 
        with open(self.basefile_path, "w") as f:
            json.dump(book_data, f, indent=4)
    

    def generate_id(self) -> int:
        """Generates a unique ID for a book"""
        return max(book.id for book in self.books) + 1 if self.books else 1

    

    def add_book(self, title: str, author: str, year: int):
        """Adds a book to the library"""
        book = Book(self.generate_id(), title, author, year)
        self.books.append(book)
        self.save_books(self.books)
        print(f"Книга '{title}' добавлена")


    def delete_book(self, book_id: int):
        """Removes a book from the library"""
        try:
            book_id = int(book_id)
        except ValueError:
            print("Некорректный ID книги")
            return
        
        book_found = False
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                book_found = True
                break

        if not book_found:
            print(f"Книга с ID {book_id} не найдена")
            return
        
        self.save_books(self.books)
        print(f"Книга с ID {book_id} удалена")

    
    def search_book(self, search_term: str|int):
        """Searches books by title, author or year"""
        results = [book for book in self.books if search_term.lower() in book.title.lower() or \
                                                search_term.lower() in book.author.lower() or \
                                                search_term == int(book.year)]
        if results:
            for book in results:
                print(book)
            return results
        else:
            print('Книги по запросу отсутствуют')


    def display_books(self):
        """Function to display all books in the library"""
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста")


    def change_book_status(self, book_id: int, new_status: str):
        """Changes the status of a book"""
        try:
            book_id = int(book_id)
        except ValueError:
            print("Некорректный ID книги")
            return

        valid_statuses = ["в наличии", "выдана"]
        if new_status not in valid_statuses:
            print("Неверный статус. Допустимые статусы: 'в наличии', 'выдана'")
            return

        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books(self.books)
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'")
                return
        print(f"Книга с ID {book_id} не найдена")



