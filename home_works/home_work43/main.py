from flask import Flask, render_template, url_for, request, flash, session, redirect

# Создание экземпляра приложения Flask
app = Flask(__name__)

# Конфигурация приложения с секретным ключом для сессий и защиты от CSRF
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Список элементов меню, каждый элемент содержит имя и URL для маршрута
menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Запись на СТО', 'url': 'appointment'},
    {'name': 'Оставить отзыв', 'url': 'comments'},
    {'name': 'Посмотреть отзывы', 'url': 'reviews'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'},
    {'name': 'Авторизация', 'url': 'login'},
    {"name": "Выйти из аккаунта", "url": "logout"}
]


# Обработчик маршрута для главной страницы и индекса
@app.route('/')
@app.route('/index')
def index():
    # URL фонового изображения для главной страницы
    background_image_url = 'https://wp-s.ru/wallpapers/12/1/425452844635038/zapchasti-dlya-avtomobilej-ch-rno-beloe-foto.jpg'
    # Рендеринг шаблона index.html с параметрами
    return render_template('index.html', background_image_url=background_image_url, title='Главная страница', menu=menu)


# Обработчик маршрута для страницы "О сайте"
@app.route('/about')
def about():
    # URL фонового изображения для страницы "О сайте"
    background_image_url = 'https://bogatyr.club/uploads/posts/2023-03/1678229039_bogatyr-club-p-detali-avtomobilya-foni-krasivo-85.jpg'
    # Рендеринг шаблона description.html с параметрами
    return render_template('description.html', background_image_url=background_image_url, title='О сайте', menu=menu)


# Обработчик маршрута для профиля пользователя
@app.route('/profile/<username>')
def profile(username):
    # Возвращает строку с именем пользователя
    return f"Пользователь: {username}"


# Обработчик маршрута для страницы "Обратная связь", поддерживающий методы GET и POST
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    # URL фонового изображения для страницы "Обратная связь"
    background_image_url = 'https://avatars.mds.yandex.net/get-altay/4396925/2a00000178b07743af0342f64365936b2e5f/diploma'
    if request.method == 'POST':
        # Проверка длины имени пользователя
        if len(request.form['username']) > 2:
            # Сообщение об успешной отправке
            flash("Сообщение отправлено успешно", category='success')
            print(request.form)
        else:
            # Сообщение об ошибке отправки
            flash("Ошибка отправки", category='error')
    # Рендеринг шаблона contact.html с параметрами
    return render_template('contact.html', background_image_url=background_image_url, title='Обратная связь', menu=menu)


# Обработчик маршрута для страницы "Комментарии", поддерживающий методы GET и POST
@app.route('/comments', methods=['POST', 'GET'], endpoint='comments')
def comments_view():
    if 'comments' not in session:
        # Инициализация пустого списка комментариев в сессии
        session['comments'] = []

    if request.method == 'POST':
        # Получение текста комментария и имени пользователя из формы
        comment_text = request.form['comment']
        username = request.form['username']

        # Проверка длины текста комментария и имени пользователя
        if len(comment_text) > 0 and len(username) > 2:
            # Генерация уникального идентификатора для комментария
            comment_id = len(session['comments'])
            # Добавление комментария в сессию
            session['comments'].append({'id': comment_id, 'username': username, 'comment': comment_text})
            # Сообщение об успешном добавлении комментария
            flash('Комментарий успешно добавлен', 'success')
        else:
            # Сообщение об ошибке добавления комментария
            flash('Ошибка добавления комментария', 'error')

        print(session)

    # URL фонового изображения для страницы "Комментарии"
    background_image_url = 'https://storage.myseldon.com/news-pict-b4/B4E9F78AE1C540AAF1BF8405F985C9F9'
    # Рендеринг шаблона comments.html с параметрами
    return render_template('comments.html', background_image_url=background_image_url, title='Комментарии', menu=menu,
                           comments=session['comments'])


# Обработчик маршрута для страницы "Отзывы", поддерживающий методы GET и POST
@app.route('/reviews', methods=['POST', 'GET'], endpoint='reviews')
def reviews():
    if 'comments' not in session:
        # Инициализация пустого списка комментариев в сессии
        session['comments'] = []

    if request.method == 'POST':
        # Получение текста отзыва и имени пользователя из формы
        comment_text = request.form['comment']
        username = request.form['username']

        # Проверка длины текста отзыва и имени пользователя
        if len(comment_text) > 0 and len(username) > 2:
            # Генерация уникального идентификатора для отзыва
            comment_id = len(session['comments'])
            # Добавление отзыва в сессию
            session['comments'].append({'id': comment_id, 'username': username, 'comment': comment_text})
            # Сообщение об успешном добавлении отзыва
            flash('Отзыв добавлен', 'success')
        else:
            # Сообщение об ошибке добавления отзыва
            flash('Ошибка добавления отзыва', 'error')

        # Перенаправление на страницу "Отзывы"
        return redirect(url_for('reviews'))

    # URL фонового изображения для страницы "Отзывы"
    background_image_url = 'https://sun9-56.userapi.com/impf/QeyBdirIKDFQMnNmBWQz7CqvXLXLfeMV3_ClcQ/ehpCjgutGvc.jpg?size=1920x768&quality=95&crop=0,14,1280,511&sign=5b457407b33b1e27828cdd619eafd915&type=cover_group'
    # Рендеринг шаблона reviews.html с параметрами
    return render_template('reviews.html', background_image_url=background_image_url, title='Отзывы', menu=menu,
                           comments=session['comments'])


# Обработчик маршрута для страницы детального просмотра отзыва, поддерживающий метод GET
@app.route('/review/<int:comment_id>', methods=['GET'], endpoint='review')
def review(comment_id):
    if 'comments' not in session:
        # Инициализация пустого списка комментариев в сессии
        session['comments'] = []

    # Поиск комментария по идентификатору
    comment = next((c for c in session['comments'] if c['id'] == comment_id), None)
    if not comment:
        # Сообщение об ошибке, если комментарий не найден
        flash('Комментарий не найден', 'error')
        # Перенаправление на страницу "Отзывы"
        return redirect(url_for('reviews'))

    # URL фонового изображения для страницы детального просмотра отзыва
    background_image_url = 'https://storage.myseldon.com/news-pict-b4/B4E9F78AE1C540AAF1BF8405F985C9F9'
    # Рендеринг шаблона review_detail.html с параметрами
    return render_template('review_detail.html', background_image_url=background_image_url, title='Просмотр отзыва',
                           menu=menu, comment=comment)


# Обработчик маршрута для удаления отзыва, поддерживающий метод POST
@app.route('/delete_review/<int:comment_id>', methods=['POST'])
def delete_review(comment_id):
    if 'comments' in session:
        # Удаление комментария из сессии по идентификатору
        session['comments'] = [comment for comment in session['comments'] if comment['id'] != comment_id]
        # Сообщение об успешном удалении отзыва
        flash('Отзыв удален', 'success')
    # Перенаправление на страницу "Отзывы"
    return redirect(url_for('reviews'))


# Обработчик ошибки 404
@app.errorhandler(404)
def page_not_found(error):
    background_image_url = 'https://catherineasquithgallery.com/uploads/posts/2023-01/1674247698_catherineasquithgallery-com-p-fon-serogo-tsveta-dlya-fotoshopa-foto-6.jpg'
    # Рендеринг шаблона page404.html с параметрами
    return render_template('page404.html', background_image_url=background_image_url, title='Страница не найдена', menu=menu)


# Обработчик маршрута для страницы авторизации, поддерживающий методы GET и POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    # URL фонового изображения для страницы авторизации
    background_image_url = 'https://irbis39.ru/upload/medialibrary/82f/82f57c366d7ca36b0eb0e6858e86e76e.gif'
    if request.method == 'POST':
        # Получение имени пользователя и пароля из формы
        username = request.form['username']
        password = request.form['psw']

        # Проверка учетных данных
        if username == 'admin' and password == '123456':
            # Успешная авторизация
            session['userLogged'] = True
            success_message = 'Вы успешно авторизовались'
            # Рендеринг шаблона login.html с сообщением об успехе
            return render_template('login.html', background_image_url=background_image_url,
                                   success_message=success_message, menu=menu)
        else:
            # Неверные учетные данные
            error_message = 'Неверное имя пользователя или пароль'
            # Рендеринг шаблона login.html с сообщением об ошибке
            return render_template('login.html', background_image_url=background_image_url, error_message=error_message,
                                   menu=menu)
    elif 'userLogged' in session:
        # Пользователь уже авторизован
        success_message = 'Вы успешно авторизовались'
        # Рендеринг шаблона login.html с сообщением об успехе
        return render_template('login.html', background_image_url=background_image_url, success_message=success_message,
                               menu=menu)
    else:
        # Рендеринг шаблона login.html без сообщений
        return render_template('login.html', background_image_url=background_image_url, menu=menu)


# Обработчик маршрута для выхода из аккаунта
@app.route("/logout")
def logout():
    # Удаление данных сессии пользователя
    session.pop('userLogged', None)
    # Перенаправление на главную страницу
    return redirect(url_for('index'))


# Обработчик маршрута для страницы "Запись на СТО", поддерживающий методы GET и POST
@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    # URL фонового изображения для страницы "Запись на СТО"
    background_image_url = 'https://tj-service.ru/wp-content/uploads/2023/10/automocion.jpg'
    if request.method == 'POST':
        # Получение даты и времени из формы
        date = request.form['date']
        time = request.form['time']
        # Здесь можно добавить логику для сохранения данных записи в базе данных или другие действия
        # Перенаправление на страницу успешной записи
        return redirect(url_for('appointment_success', date=date, time=time, menu=menu))
    # Рендеринг шаблона appointment.html с параметрами
    return render_template('appointment.html', background_image_url=background_image_url, title='Запись на СТО',
                           menu=menu)


# Обработчик маршрута для страницы успешной записи на СТО
@app.route('/appointment_success/<date>/<time>')
def appointment_success(date, time):
    # URL фонового изображения для страницы успешной записи
    background_image_url = 'https://tj-service.ru/wp-content/uploads/2023/10/automocion.jpg'
    # Рендеринг шаблона appointment_success.html с параметрами
    return render_template('appointment_success.html', date=date, time=time, background_image_url=background_image_url,
                           title='Запись успешно оформлена')


# Точка входа для запуска приложения
if __name__ == '__main__':
    # Запуск приложения в режиме отладки
    app.run(debug=True)
