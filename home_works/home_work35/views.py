from typing import List


def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    """
    Класс для взаимодействия с пользователем.
    """

    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self) -> str:
        """
        Ожидает ответа пользователя.
        """
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма")
    def add_user_film(self) -> dict:
        """
        Добавляет данные о фильме, введенные пользователем.
        """
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность в минутах": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            if key == "год выпуска" or key == "длительность":
                while True:
                    user_input = input(f"Введите {key} фильма: ")
                    if user_input.isdigit():
                        dict_film[key] = int(user_input)
                        break
                    else:
                        print("Ошибка: Введите целое число.")
            else:
                dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film

    @add_title("Каталог фильмов")
    def show_all_films(self, films: str) -> None:
        """
        Выводит каталог фильмов.
        """
        for index, film in enumerate(films, 1):
            print(f"{index}. {film}")

    @add_title("Ввод названия фильма")
    def get_user_film(self) -> str:
        """
        Получает название фильма от пользователя.
        """
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма")
    def show_single_film(self, film: dict) -> None:
        """
        Выводит информацию о фильме.
        """
        for key in film:
            print(f"{key} фильма - {film[key]}")

    #
    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title: str) -> None:
        """
        Выводит сообщение об ошибке при неверном названии фильма.
        """
        print(f"Фильм с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_film(self, user_title: str) -> None:
        """
        Выводит сообщение об удалении фильма.
        """
        print(f"Фильм {user_title} был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer: str) -> None:
        """
        Выводит сообщение об ошибке при неверном вводе пользователя.
        """
        print(f"Варианта {answer} не существует")
