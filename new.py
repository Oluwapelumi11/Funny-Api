from flask import Flask,jsonify
import random

from qoutes import funny_qoutes

app = Flask(__name__)

@app.route('/single')
def new():
    qoutes=funny_qoutes()
    length = len(qoutes)
    selected = qoutes[random.randint(0, length-1)]
    return jsonify(selected)

@app.route('/all')
def all():
    qoutes=funny_qoutes()
    return qoutes

if __name__ == "__main__":
    app.run(debug=True)