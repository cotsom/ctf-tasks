from crypt import methods
from datetime import date
import string
from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    date = ""
    if request.method == 'POST':
        date = os.popen(request.form['date']).read()

    return render_template('index.html', title="most accurate time", outputDate=date)

@app.errorhandler(404)
def page_not_found(e):
    route = request.path
    return str(route)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000' ,debug=False)
