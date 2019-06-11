from flask import Flask, redirect, render_template
from scrapping import *



app = Flask(__name__)

@app.route('/')
def index():
    a = Scraping()
    ticker = a.get_first_ticker()
    chart_data = a.get_dates_prices(ticker[0])
    return render_template('index.html', ticker=ticker, chart_data=chart_data)



if __name__ == '__main__':
    app.run(debug=True)


#set FLASK_APP=app.py
#set FLASK_ENV=development
