
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
poetry run library-manager display
--- Пример использования ---
poetry run library-manager display



--- Изменяет статус книги по id ---
poetry run library-manager change_status book-id "выдана" или "в наличии"
--- Пример использования ---
poetry run library-manager change_status 3 "выдана"



poetry run library-manager add "Война и мир" "Лев Толстой" 1869
poetry run library-manager add "Преступление и наказание" "Фёдор Достоевский" 1866
poetry run library-manager add "Мастер и Маргарита" "Михаил Булгаков" 1967
poetry run library-manager add "Анна Каренина" "Лев Толстой" 1878
poetry run library-manager add "Евгений Онегин" "Александр Пушкин" 1837
poetry run library-manager add "Отцы и дети" "Иван Тургенев" 1862
poetry run library-manager add "Герой нашего времени" "Михаил Лермонтов" 1840
poetry run library-manager add "Обломов" "Иван Гончаров" 1859
poetry run library-manager add "Тихий Дон" "Михаил Шолохов" 1928
poetry run library-manager add "Доктор Живаго" "Борис Пастернак" 1957
poetry run library-manager add "Палата №6" "Антон Чехов" 1892
poetry run library-manager add "Собачье сердце" "Михаил Булгаков" 1987
poetry run library-manager add "Мы" "Евгений Замятин" 1924
poetry run library-manager add "Белая гвардия" "Михаил Булгаков" 1925
poetry run library-manager add "Раковый корпус" "Александр Солженицын" 1968
poetry run library-manager add "Архипелаг ГУЛАГ" "Александр Солженицын" 1973
poetry run library-manager add "Жизнь и судьба" "Василий Гроссман" 1980
poetry run library-manager add "Один день Ивана Денисовича" "Александр Солженицын" 1962
poetry run library-manager add "Прощание с Матёрой" "Валентин Распутин" 1976
poetry run library-manager add "Дети Арбата" "Анатолий Рыбаков" 1987
poetry run library-manager add "Раковый корпус" "Александр Солженицын" 1968
poetry run library-manager add "Архипелаг ГУЛАГ" "Александр Солженицын" 1973
poetry run library-manager add "Жизнь и судьба" "Василий Гроссман" 1980
poetry run library-manager add "Один день Ивана Денисовича" "Александр Солженицын" 1962
poetry run library-manager add "Прощание с Матёрой" "Валентин Распутин" 1976
poetry run library-manager add "Дети Арбата" "Анатолий Рыбаков" 1987
