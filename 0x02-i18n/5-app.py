#!/usr/bin/env python3
"""
Mockup some users
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Babel configuration class"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """this function runs before request is sent"""
    id = request.args.get('login_as')
    if id:
        g.user = get_user(id)


@babel.localeselector
def get_locale() -> str:
    """get best match of lang to display"""
    locale = request.args.get('locale', 'en')
    if locale == 'fr':
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Index page"""

    return render_template('5-index.html')


def get_user(id: str) -> Union[dict, None]:
    """get registered user"""
    if not id:
        return None

    if id not in users.keys():
        return None

    return users[id]
