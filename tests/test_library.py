import pytest
import json, os
from unittest.mock import patch, mock_open
from library_service.library_service import Library 

db_file_path = 'test_path.json'

@pytest.fixture
def mock_json_data():
    return json.dumps([
        {"id": 1, "title": "Oliver Twist", "author": "Charles Dickens", "year": 1837, "status": "в наличии"},
        {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "status": "в наличии"}
    ])


@pytest.fixture
def library(mock_json_data):
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        lib = Library(db_file_path)
    yield lib
    # Удаляем файл базы данных после выполнения тестов
    if os.path.exists(db_file_path):
        os.remove(db_file_path)




def test_load_books(library):
    assert len(library.books) == 2
    assert library.books[0].title == "Oliver Twist"
    assert library.books[1].author == "Jane Austen"
    library.basefile_path = 'fake_path.json'
    assert library.load_books() == []


def test_add_book(library):
    library.add_book("Книга 3", "Автор 3", 2003)
    assert len(library.books) == 3
    assert library.books[-1].title == "Книга 3"


def test_delete_book(library, capsys):
    library.delete_book('word')
    captured = capsys.readouterr()
    assert captured.out == "Invalid book ID\n"

    library.delete_book(12)
    captured = capsys.readouterr()
    assert captured.out == 'Book with ID 12 not found\n'

    assert len(library.books) == 2
    library.delete_book(1)
    assert len(library.books) == 1
    assert library.books[0].id == 2



def test_search_book_by_title(library, capsys):
    search_results = library.search_book("Oliver Twist")
    capsys.readouterr()
    assert len(search_results) == 1
    assert search_results[0].title == "Oliver Twist"
    search_results = library.search_book("Sense and Sensibility")
    captured = capsys.readouterr()
    assert captured.out == 'There are no books on request\n'

def test_change_book_status(library, capsys):
    library.change_book_status('word', "выдана")
    captured = capsys.readouterr()
    assert captured.out == 'Invalid book ID\n'

    library.change_book_status(1, "random string")
    captured = capsys.readouterr()
    assert captured.out == "Invalid status. Acceptable statuses: 'в наличии', 'выдана'\n"

    library.change_book_status(12, "выдана")
    captured = capsys.readouterr()
    assert captured.out == "Book with ID 12 not found\n"

    library.change_book_status(1, "выдана")
    assert library.books[0].status == "выдана"
    
    library.change_book_status(2, "в наличии")
    assert library.books[1].status == "в наличии"


def test_display_books(library, capsys):
    library.all_books()  # Check for outputs if needed
    captured = capsys.readouterr()
    assert captured.out == 'ID: 1, Title: Oliver Twist, Author: Charles Dickens, Year: 1837, Status: в наличии\nID: 2, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813, Status: в наличии\n'
    library.delete_book(1)
    library.delete_book(2)
    capsys.readouterr()
    library.all_books()
    captured = capsys.readouterr()
    assert captured.out == 'The library is empty\n'

