import argparse
from .library_service import Library


basefile_path = "library.json"


def cli():

    library = Library(basefile_path)

    parser = argparse.ArgumentParser(description='Library management application')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Добавление книги
    add_parser = subparsers.add_parser('add', help='Add a new book')
    add_parser.add_argument('title', type=str, help='Title of the book')
    add_parser.add_argument('author', type=str, help='Author of the book')
    add_parser.add_argument('year', type=int, help='Year of publication')

    # Удаление книги
    delete_parser = subparsers.add_parser('delete', help='Delete a book')
    delete_parser.add_argument('book_id', type=str, help='ID of the book to delete')

    # Поиск книги
    search_parser = subparsers.add_parser('search', help='Search for books')
    search_parser.add_argument('search_term', type=str, help='Search term (title, author, or year)')

    # Отображение всех книг
    subparsers.add_parser('all_books', help='Display all books')

    # Изменение статуса книги
    change_status_parser = subparsers.add_parser('change_status', help='Change book status')
    change_status_parser.add_argument('book_id', type=str, help='ID of the book')
    change_status_parser.add_argument('new_status', type=str, help='New status ("в наличии" or "выдана")')

    args = parser.parse_args()


    if args.command == 'add':
        library.add_book(args.title, args.author, args.year)
    elif args.command == 'delete':
        library.delete_book(args.book_id)
    elif args.command == 'search':
        library.search_book(args.search_term)
    elif args.command == 'all_books':
        library.all_books()
    elif args.command == 'change_status':
        library.change_book_status(args.book_id, args.new_status)
    else:
        parser.print_help()
