#!/usr/bin/env python3
"""
Babel Config module
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


@app.route('/')
def index() -> str:
    """Index page"""
    return render_template('1-index.html')
