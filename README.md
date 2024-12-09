# Library Service Command Line Interface
## Use Cases
  Команда|Описание
  -|-|-
  poetry run library-service add "Название" "Автор" Год | Добавление новой книги
Скачайте и распакуйте архив с проектом

Затем перейдите в папку с проектом с помощью командной строки используя команду cd 

Пример [ cd C:\test-task-library--master ]

Установите poetry
[ pip install poetry ]

Установите зависимости проекта
[ poetry install ]

Запуск теста
[ poetry run pytest ]

Запуск теста c отображением процента покрытия
[ poetry run pytest --cov ]

Команды менеджмента библиотеки:


--- Добавить новую книгу ---

poetry run library-service add "Название" "Автор" Год

--- Пример использования ---

poetry run library-service add "Война и мир" "Лев Толстой" 1869


--- Удалить книгу по id ---

poetry run library-service delete book-id

--- Пример использования ---

poetry run library-service delete 2


--- Поиск книги по названию, автору или году ---

poetry run library-service search "Название" или "Автор" или Год

--- Пример использования ---

poetry run library-service search "Война и мир"


--- Показать все книги которые находятся в библиотеке ---

poetry run library-service all_books

--- Пример использования ---

poetry run library-service all_books


--- Изменяет статус книги по id ---

poetry run library-service change_status book-id "выдана" или "в наличии"

--- Пример использования ---

poetry run library-service change_status 3 "выдана"
