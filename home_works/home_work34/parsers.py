import csv
import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    """
    Получает HTML-код страницы по заданному URL.
    """
    r = requests.get(url)
    return r.text


def get_data(html: str) -> None:
    """
    Извлекает данные о постах (название, URL, описание, просмотры) из HTML-кода.
    """
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("article", class_="post-box")

    for el in elements:
        try:
            name = el.find("span", itemprop="headline").text
        except AttributeError:
            name = ""

        try:
            url = el.find("h2").find("a")["href"]
        except AttributeError:
            url = ""

        try:
            description = el.find("p").text.strip()
        except AttributeError:
            description = ""

        try:
            view = el.find("span", class_="entry-meta__views").text.strip()
        except AttributeError:
            view = ""

        data = {
            "name": name,
            "url": url,
            "description": description,
            "view": view,
        }

        write_csv(data)


def write_csv(data: dict) -> None:
    """
    Записывает данные в CSV файл.
    """
    with open("addons_wow.csv", "a", encoding="windows-1251") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data["name"], data["url"], data["description"], data["view"]))


def main() -> None:
    """
    Основная функция для выполнения скрипта.
    """
    for i in range(1, 8):
        url = f"https://wow-sirus.ru/category/addony/page/{i}/"
        get_data(get_html(url))


if __name__ == '__main__':
    main()
