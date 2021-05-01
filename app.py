'''Modulo para correr el webserver con Flask'''
from flask import Flask,render_template, request
from scrapping import scrappingUdemy

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def upload_file():

    return render_template("index.html", data=scrappingUdemy())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
