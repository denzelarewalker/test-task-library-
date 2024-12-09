# Library Service Command Line Interface

* Скачайте и распакуйте архив с проектом

* Затем перейдите в папку с проектом с помощью командной строки используя команду cd 

Пример `cd C:\test-task-library--master`

* Установите poetry `pip install poetry`

* Установите зависимости проекта `poetry install`




## Use Cases
  Команда|Описание
  -|-
  `poetry run library-service add "Название" "Автор" Год`<br><br>Пример<br>`poetry run library-service add "Война и мир" "Лев Толстой" 1869` | Добавление новой книги
  `poetry run library-service delete book-id`<br><br>Пример<br>`poetry run library-service delete 1` | Удаление книги по id
  `poetry run library-service search "Название"`<br>`poetry run library-service search "Автор"`<br>`poetry run library-service search Год`<br><br>Пример<br>`poetry run library-service search "Война и мир"` | Поиск книги по названию, автору или году
  `poetry run library-service all_books` | Показать все книги в библиотеке
  `poetry run library-service change_status book-id "выдана"`<br>`poetry run library-service change_status book-id "в наличии"` | Изменить статус книги по id

## Tests
  Запуск теста|Запуск теста c отображением процента покрытия
  -|-
  `poetry run pytest` | `poetry run pytest --cov`
