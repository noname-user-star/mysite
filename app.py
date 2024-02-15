import os
from flask import Flask, render_template, url_for
import app

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/generic/<id>")
def generic_theme(id):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    filepath = os.path.join(__location__, f"theme_{int(id)}.txt")
    with open(filepath, mode="r+", encoding="utf-8") as file:
        content = file.read()
    return render_template("generic.html", context=content)

if __name__ == "__main__":
    app.run()