from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    address = 5
    return render_template('index.html', address=address)
