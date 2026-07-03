from flask import Blueprint, render_template, request, jsonify
from tranliterator import *

main = Blueprint("main", __name__)

@main.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")


@main.route("/api/tranlite/", methods=["POST"])
def tranlite():
    data = request.get_json()
    text = data.get('sourceText', '')
    from_to = data.get('Translite','')

    print(data)
    print(type(data))
    print(from_to)
    print(type(from_to))

    if from_to.lower().startswith("latin"):
        result = latin_to_cyrillic(text)
    else:
        result = cyrillic_to_latin(text)

    return jsonify({'tranliterated': result})
