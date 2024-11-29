Скачайте и распакуйте архив. 
Затем перейдите в папку с проектом с помощью командной строки используя команду cd 


Пример [ cd C:\test-task-library--master ]


--- Добавить новую книгу ---
poetry run library-manager add "Название" "Автор" Год
--- Пример использования ---
poetry run library-manager add "Война и мир" "Лев Толстой" 1869



--- Удалить книгу по id ---
poetry run library-manager delete book-id
--- Пример использования ---
poetry run library-manager delete 2



--- Поиск книги по названию, автору или году ---
poetry run library-manager search "Название" или "Автор" или Год
--- Пример использования ---
poetry run library-manager search "Война и мир"



--- Показать все книги которые находятся в библиотеке ---
poetry run library-manager all_books
--- Пример использования ---
poetry run library-manager all_books



--- Изменяет статус книги по id ---
poetry run library-manager change_status book-id "выдана" или "в наличии"
--- Пример использования ---
poetry run library-manager change_status 3 "выдана"


