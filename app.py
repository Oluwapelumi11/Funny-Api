from flask import Flask,jsonify
import random
from qoutes import funny_qoutes


app = Flask(__name__)


@app.route("/api/funny/single")
def serve_funny_qoute():
    qoutes = funny_qoutes()
    nr_of_qoutes=len(qoutes)
    selected = qoutes[random.randint(0,nr_of_qoutes -1)]
    return jsonify(selected)


@app.route('/api/funny/all')
def all():
    qoutes=funny_qoutes()
    return qoutes

if __name__=="__main__":
    app.run(debug=True)