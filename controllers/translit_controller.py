from flask import Blueprint, render_template, request, jsonify
from tranliterator import *

main = Blueprint("main", __name__)

@main.route("/", methods = ["GET", "POST"])
def index():
    locale = request.accept_languages.best_match(["en", "ru"])
    print("Detected locale:", locale)
    return render_template("index.html")


@main.route("/api/tranlite/<lang>", methods=["POST"])
def tranlite(lang):
    data = request.get_json()
    text = data.get('sourceText', '')
    from_to = data.get('Translite','')

    if from_to.lower().startswith("latin"):
        result = latin_to_cyrillic(text, lang)
    else:
        result = cyrillic_to_latin(text, lang)

    return jsonify({'tranliterated': result})
