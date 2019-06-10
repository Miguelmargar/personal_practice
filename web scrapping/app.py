from flask import Flask, redirect, render_template
from scrapping import *



app = Flask(__name__)

@app.route('/')
def index():
    a = Scraping()
    ticker = a.get_first_ticker()
    return render_template('index.html', ticker=ticker)



if __name__ == '__main__':
    app.run(debug=True)


#set FLASK_APP=app.py
#set FLASK_ENV=development
