from views import UserInterface
from models import FilmModel


class Controller:
    """
    Контроллер, управляющий взаимодействием между моделью и представлением.
    """
    def __init__(self):
        """
        Инициализирует объект контроллера.
        """
        self.film_model = FilmModel()  # Model
        self.user_interface = UserInterface()  # View

    def run(self) -> None:
        """
        Запускает основной цикл приложения.
        """
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer: str) -> None:
        """
        Проверяет ответ пользователя и выполняет соответствующие действия.
        """

        if answer == "1":
            film = self.user_interface.add_user_film()
            self.film_model.add_film(film)

        elif answer == "2":
            films = self.film_model.get_all_films()
            self.user_interface.show_all_films(films)

        elif answer == "3":
            films_title = self.user_interface.get_user_film()
            try:
                film = self.film_model.get_single_film(films_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(films_title)
            else:
                self.user_interface.show_single_film(film)

        elif answer == "4":
            films_title = self.user_interface.get_user_film()
            try:
                self.film_model.remove_film(films_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(films_title)
            else:
                self.user_interface.remove_single_film(films_title)

        elif answer == "q":
            self.film_model.save_data()

        else:
            self.user_interface.show_incorrect_answer_error(answer)

