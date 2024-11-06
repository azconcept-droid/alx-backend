#!/usr/bin/env python3
"""
Parametrize templates module
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, lazy_gettext as _l


class Config:
    """Babel configuration class"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get best match of lang to display"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Index page"""
    return render_template('3-index.html',
                           home_title=_l('Welcome to Holberton'),
                           home_header=_l('Hello world'))
