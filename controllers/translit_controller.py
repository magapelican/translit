from flask import Blueprint, render_template, request, jsonify
from tranliterator import *

main = Blueprint("main", __name__)

@main.route("/", methods = ["GET", "POST"])
def index():
    locale = request.accept_languages.best_match(["en", "ru"])
    print("Detected locale:", locale)
    return render_template("index.html")


@main.route("/api/tranlite/", methods=["POST"])
def tranlite():
    data = request.get_json()
    text = data.get('sourceText', '')
    from_to = data.get('Translite','')

    if from_to.lower().startswith("latin"):
        result = latin_to_cyrillic(text)
    else:
        result = cyrillic_to_latin(text)

    return jsonify({'tranliterated': result})
