# Library Service Command Line Interface

* Скачайте и распакуйте архив с проектом

* Затем перейдите в папку с проектом с помощью командной строки используя команду cd 

Пример `cd C:\test-task-library--master`

* Установите poetry `pip install poetry`

* Установите зависимости проекта `poetry install`


  Запуск теста|Запуск теста c отображением процента покрытия
  -|-
  `poetry run pytest` | `poetry run pytest --cov`

## Use Cases
  Команда|Описание
  -|-
  poetry run library-service add "Название" "Автор" Год | Добавление новой книги
  poetry run library-service delete book-id | Удаление книги по id
  poetry run library-service search "Название" или "Автор" или Год | Поиск книги по названию, автору или году
  poetry run library-service all_books | Показать все книги в библиотеке
  poetry run library-service change_status book-id "выдана" или "в наличии" | Изменить статус книги по id
