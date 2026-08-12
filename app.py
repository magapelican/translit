from flask import Flask, request
from flask_babel import Babel
from controllers.translit_controller import main

app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'ru']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app, locale_selector=lambda: request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES']))

app.register_blueprint(main)


if __name__ == "__main__":
    app.run(debug=True)