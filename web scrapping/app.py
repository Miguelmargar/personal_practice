from flask import Flask, render_template
from scrapping import *


app = Flask(__name__)


@app.route('/')
def main():

    return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True)


#set FLASK_APP=api.py
#set FLASK_ENV=development
