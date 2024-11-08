#!/usr/bin/env python3
"""
Config babel using get_locale function
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return render_template('2-index.html')
