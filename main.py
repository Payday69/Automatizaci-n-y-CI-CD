from flask import Flask, jsonify, request
from .math_utils import add, multiply
from .string_utils import capitalize_words, reverse_text

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "API de CI/CD funcionando correctamente"})

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.json
    result = add(data["a"], data["b"])
    return jsonify({"resultado": result})

@app.route("/capitalize", methods=["POST"])
def capitalize_text():
    data = request.json
    result = capitalize_words(data["text"])
    return jsonify({"resultado": result})

if __name__ == "__main__":
    app.run(debug=True)
