"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask
from flask import request
from flask import render_template
from werkzeug.exceptions import NotFound

from views.app import about_app


app = Flask (__name__)


app.register_blueprint(about_app)


app.config.update(
    ENV="development",
    SECRET_KEY="dfhgdsGDSAGSDgsfdhgerGFASD",
)


def print_request():
    print("request:", request)
    print("headers", request.headers)


@app.route("/", endpoint="index_page")
def get_root():
    return render_template("index.html")


@app.errorhandler(404)
def handle_404(error):
    if isinstance(error, NotFound) and error.description != NotFound.description:
        return error
    return f"<h1>error: {error}</h1>", 404


if __name__ == "__main__":
    app.run(
        debug=True,
        )