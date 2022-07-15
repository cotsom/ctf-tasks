import string
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="most accurate time")

@app.route("/handler/<index>/", methods=["GET", "POST"])
def handler(index):
    output = os.popen('date').read()
    return str(output)



if __name__ == "__main__":
    app.run(debug=True)
