import pytest
import json, os
from unittest.mock import patch, mock_open
from library_service import Library 

db_file_path = 'test_path.json'

@pytest.fixture
def mock_json_data():
    """Mock JSON data for the library"""
    return json.dumps([
        {"id": 1, "title": "Книга 1", "author": "Автор 1", "year": 2001, "status": "в наличии"},
        {"id": 2, "title": "Книга 2", "author": "Автор 2", "year": 2002, "status": "в наличии"}
    ])


@pytest.fixture
def library(mock_json_data):
    """Fixture for Library instance with mocked JSON data"""
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        lib = Library(db_file_path)
    yield lib
    # Удаляем файл базы данных после выполнения тестов
    if os.path.exists(db_file_path):
        os.remove(db_file_path)




def test_load_books(library):
    """Test loading books from JSON"""
    assert len(library.books) == 2
    assert library.books[0].title == "Книга 1"
    assert library.books[1].author == "Автор 2"
    library.basefile_path = 'fake_path.json'
    assert library.load_books() == []


def test_add_book(library):
    """Test adding a book"""
    library.add_book("Книга 3", "Автор 3", 2003)
    assert len(library.books) == 3
    assert library.books[-1].title == "Книга 3"


def test_delete_book(library, capsys):
    """Test deleting a book"""
    library.delete_book('word')
    captured = capsys.readouterr()
    assert captured.out == "Некорректный ID книги\n"

    library.delete_book(12)
    captured = capsys.readouterr()
    assert captured.out == 'Книга с ID 12 не найдена\n'

    assert len(library.books) == 2
    library.delete_book(1)
    assert len(library.books) == 1
    assert library.books[0].id == 2



def test_search_book_by_title(library, capsys):
    """Test searching book by title"""
    search_results = library.search_book("Книга 1")
    capsys.readouterr()
    assert len(search_results) == 1
    assert search_results[0].title == "Книга 1"
    search_results = library.search_book("Книга 3")
    captured = capsys.readouterr()
    assert captured.out == 'Книги по запросу отсутствуют\n'

def test_change_book_status(library, capsys):
    """Test changing the status of a book"""
    library.change_book_status('word', "выдана")
    captured = capsys.readouterr()
    assert captured.out == 'Некорректный ID книги\n'

    library.change_book_status(1, "random string")
    captured = capsys.readouterr()
    assert captured.out == "Неверный статус. Допустимые статусы: 'в наличии', 'выдана'\n"

    library.change_book_status(12, "выдана")
    captured = capsys.readouterr()
    assert captured.out == "Книга с ID 12 не найдена\n"

    library.change_book_status(1, "выдана")
    assert library.books[0].status == "выдана"
    
    library.change_book_status(2, "в наличии")
    assert library.books[1].status == "в наличии"


def test_display_books(library, capsys):
    """Test displaying books"""
    library.display_books()  # Check for outputs if needed
    captured = capsys.readouterr()
    assert captured.out == 'ID: 1, Название: Книга 1, Автор: Автор 1, Год: 2001, Статус: в наличии\nID: 2, Название: Книга 2, Автор: Автор 2, Год: 2002, Статус: в наличии\n'
    library.delete_book(1)
    library.delete_book(2)
    capsys.readouterr()
    library.display_books()
    captured = capsys.readouterr()
    assert captured.out == 'Библиотека пуста\n'


if __name__ == "__main__":
    pytest.main()
