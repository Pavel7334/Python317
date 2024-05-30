from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'}
]


@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная страница', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route('/profile/<int:username>')
def profile(username):
    return f"Пользователь {username}"


if __name__ == '__main__':
    app.run(debug=True)

