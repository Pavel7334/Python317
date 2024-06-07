from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

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


@app.route('/')
@app.route('/index')
def index():
    background_image_url = 'https://wp-s.ru/wallpapers/12/1/425452844635038/zapchasti-dlya-avtomobilej-ch-rno-beloe-foto.jpg'
    return render_template('index.html', background_image_url=background_image_url, title='Главная страница', menu=menu)


@app.route('/about')
def about():
    background_image_url = 'https://bogatyr.club/uploads/posts/2023-03/1678229039_bogatyr-club-p-detali-avtomobilya-foni-krasivo-85.jpg'
    return render_template('about.html', background_image_url=background_image_url, title='О сайте', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    return f"Пользователь: {username}"


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    background_image_url = 'https://avatars.mds.yandex.net/get-altay/4396925/2a00000178b07743af0342f64365936b2e5f/diploma'
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно", category='success')
            print(request.form)
        else:
            flash("Ошибка отправки", category='error')
    return render_template('contact.html', background_image_url=background_image_url, title='Обратная связь', menu=menu)


@app.route('/comments', methods=['POST', 'GET'], endpoint='comments')
def comments_view():
    if 'comments' not in session:
        session['comments'] = []

    if request.method == 'POST':
        comment_text = request.form['comment']
        username = request.form['username']

        if len(comment_text) > 0 and len(username) > 2:
            comment_id = len(session['comments'])  # Генерируем уникальный идентификатор
            session['comments'].append({'id': comment_id, 'username': username, 'comment': comment_text})
            flash('Комментарий успешно добавлен', 'success')
        else:
            flash('Ошибка добавления комментария', 'error')

        print(session)

    background_image_url = 'https://storage.myseldon.com/news-pict-b4/B4E9F78AE1C540AAF1BF8405F985C9F9'
    return render_template('comments.html', background_image_url=background_image_url, title='Комментарии', menu=menu, comments=session['comments'])


@app.route('/reviews', methods=['POST', 'GET'], endpoint='reviews')
def reviews():
    if 'comments' not in session:
        session['comments'] = []

    if request.method == 'POST':
        comment_text = request.form['comment']
        username = request.form['username']

        if len(comment_text) > 0 and len(username) > 2:
            comment_id = len(session['comments'])  # Генерируем уникальный идентификатор
            session['comments'].append({'id': comment_id, 'username': username, 'comment': comment_text})
            flash('Отзыв добавлен', 'success')
        else:
            flash('Ошибка добавления отзыва', 'error')

        return redirect(url_for('reviews'))

    background_image_url = 'https://sun9-56.userapi.com/impf/QeyBdirIKDFQMnNmBWQz7CqvXLXLfeMV3_ClcQ/ehpCjgutGvc.jpg?size=1920x768&quality=95&crop=0,14,1280,511&sign=5b457407b33b1e27828cdd619eafd915&type=cover_group'
    return render_template('reviews.html', background_image_url=background_image_url, title='Отзывы', menu=menu, comments=session['comments'])


@app.route('/review/<int:comment_id>', methods=['GET'], endpoint='review')
def review(comment_id):
    if 'comments' not in session:
        session['comments'] = []

    comment = next((c for c in session['comments'] if c['id'] == comment_id), None)
    if not comment:
        flash('Комментарий не найден', 'error')
        return redirect(url_for('reviews'))

    background_image_url = 'https://storage.myseldon.com/news-pict-b4/B4E9F78AE1C540AAF1BF8405F985C9F9'
    return render_template('review_detail.html', background_image_url=background_image_url, title='Просмотр отзыва', menu=menu, comment=comment)


@app.route('/delete_review/<int:comment_id>', methods=['POST'])
def delete_review(comment_id):
    if 'comments' in session:
        session['comments'] = [comment for comment in session['comments'] if comment['id'] != comment_id]
        flash('Отзыв удален', 'success')
    return redirect(url_for('reviews'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


@app.route('/login', methods=['GET', 'POST'])
def login():
    background_image_url = 'https://irbis39.ru/upload/medialibrary/82f/82f57c366d7ca36b0eb0e6858e86e76e.gif'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']

        if username == 'admin' and password == '123456':
            # Успешная авторизация
            session['userLogged'] = True
            success_message = 'Вы успешно авторизовались'
            return render_template('login.html', background_image_url=background_image_url,
                                   success_message=success_message, menu=menu)
        else:
            # Неверные учетные данные
            error_message = 'Неверное имя пользователя или пароль'
            return render_template('login.html', background_image_url=background_image_url, error_message=error_message,
                                   menu=menu)
    elif 'userLogged' in session:
        # Пользователь авторизован
        success_message = 'Вы успешно авторизовались'
        return render_template('login.html', background_image_url=background_image_url, success_message=success_message,
                               menu=menu)
    else:
        return render_template('login.html', background_image_url=background_image_url, menu=menu)


@app.route("/logout")
def logout():
    session.pop('userLogged', None)  # Удаляем данные сессии
    return redirect(url_for('index'))


@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    background_image_url = 'https://tj-service.ru/wp-content/uploads/2023/10/automocion.jpg'
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        # Здесь можно добавить логику для сохранения данных записи в базе данных или другие действия

        return redirect(url_for('appointment_success', date=date, time=time, menu=menu))

    return render_template('appointment.html', background_image_url=background_image_url, title='Запись на СТО',
                           menu=menu)


@app.route('/appointment_success/<date>/<time>')
def appointment_success(date, time):
    background_image_url = 'https://tj-service.ru/wp-content/uploads/2023/10/automocion.jpg'
    return render_template('appointment_success.html', date=date, time=time, background_image_url=background_image_url,
                           title='Запись успешно оформлена')


if __name__ == '__main__':
    app.run(debug=True)
