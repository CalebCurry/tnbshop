from flask import Flask, render_template
app = Flask(__name__)

address = 5


@app.route('/')
def hello_world():
    return render_template('index.html', address=address)


@app.route('/data')
def data():
    return str(address)
