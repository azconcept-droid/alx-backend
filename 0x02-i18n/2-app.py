#!/usr/bin/env python3
"""
Config babel using get_locale function
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get best match of lang to display"""
    return request.accept_languages.best_match(app.config['en', 'fr'])


@app.route('/')
def index() -> str:
    """Index page"""
    return render_template('2-index.html')
