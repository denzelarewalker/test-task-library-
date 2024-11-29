import pytest
import json, os
from unittest.mock import patch, mock_open
from library_management import Library 

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


def test_add_book(library):
    """Test adding a book"""
    library.add_book("Книга 3", "Автор 3", 2003)
    assert len(library.books) == 3
    assert library.books[-1].title == "Книга 3"


def test_delete_book(library):
    """Test deleting a book"""
    library.delete_book(1)
    assert len(library.books) == 1
    assert library.books[0].id == 2


def test_search_book_by_title(library):
    """Test searching book by title"""
    search_results = library.search_book("Книга 1")
    assert len(search_results) == 1
    assert search_results[0].title == "Книга 1"


def test_change_book_status(library):
    """Test changing the status of a book"""
    library.change_book_status(1, "выдана")
    assert library.books[0].status == "выдана"
    
    library.change_book_status(2, "в наличии")
    assert library.books[1].status == "в наличии"





if __name__ == "__main__":
    pytest.main()
