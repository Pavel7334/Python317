from controllers import Controller


def main() -> None:
    """
    Главная функция приложения, запускающая контроллер.
    """
    app = Controller()
    app.run()


if __name__ == "__main__":
    main()