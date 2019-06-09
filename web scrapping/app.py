from flask import Flask, redirect, render_template, request
from scrapping import *


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


#set FLASK_APP=app.py
#set FLASK_ENV=development
