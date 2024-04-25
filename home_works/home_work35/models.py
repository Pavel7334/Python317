import pickle
import os.path
from typing import List, Dict, Any


class Film:
    """
    Представляет фильм с различными атрибутами.
    """
    def __init__(self, title: str, genre: str, director: str, year_release: int,
                 duration: int, atelier: str, actors: List[str]):
        """
        Инициализирует объект Film.
        """
        self.title = title
        self.genre = genre
        self.director = director
        self.year_release = year_release
        self.duration = duration
        self.atelier = atelier
        self.actors = actors

    def __str__(self) -> str:
        return f"{self.title} ({self.director})"


class FilmModel:
    """
        Представляет модель для управления фильмами.
    """
    def __init__(self):
        """
            Инициализирует объект FilmModel.
        """
        self.db_name = "db.txt"
        self.films: Dict[str, Film] = self.load_data()

    def add_film(self, dict_film: Dict[str, Any]) -> Film:
        """
        Добавляет фильм в модель на основе переданного словаря.
        """
        film = Film(*dict_film.values())
        self.films[film.title] = film
        return film

    def get_all_films(self) -> List[Film]:
        """
        Возвращает список всех фильмов в модели.
        """
        return list(self.films.values())

    def get_single_film(self, user_title: str) -> Dict[str, Any]:
        """
        Возвращает информацию о конкретном фильме по его названию.
        """
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссера": film.director,
            "год выпуска": film.year_release,
            "длительность": film.duration,
            "студию": film.atelier,
            "актеров": film.actors
        }
        return dict_film

    def remove_film(self, user_title: str) -> Film:
        """
        Удаляет фильм из модели по его названию.
        """
        return self.films.pop(user_title)

    def save_data(self) -> None:
        """
        Сохраняет данные модели в файл.
        """
        with open(self.db_name, "wb") as file:
            pickle.dump(self.films, file)

    def load_data(self) -> Dict[str, Film]:
        """
        Загружает данные модели из файла, если такой существует.
        """
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as file:
                return pickle.load(file)
        else:
            return {}
