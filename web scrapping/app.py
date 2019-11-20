from flask import Flask, redirect, render_template, request, flash
from scrapping import *
from users import *



app = Flask(__name__)
app.secret_key = flash_key

# @app.route('/')
# def index():
#     a = Scraping()
# 
#     # if not auth:
#     ticker = a.get_first_ticker()
#     # if auth:
#     # ticker = a.get_all_last_info()
# 
#     # chart work
#     str_ticker = [ticker[0]]
#     chart_data = a.get_dates_prices_chart(ticker[0]) 
#     return render_template('index.html', ticker=ticker, str_ticker=str_ticker, chart_data=chart_data)


@app.route('/')
def index():
    return render_template("finance.html")

@app.route('/signUp', methods=['POST'])
def signup():
    user_name = request.form.get("upName")
    email = request.form.get("upEmail")
    password = request.form.get("upPass")
    
    user = Users()
    signup = user.sign_user_up(user_name, email, password)
    
    if signup:
        flash("%s, Your account Has been Created" % user_name)
    else:
        flash("Name '%s' or '%s' is Already Taken, Please try again!" % (user_name, email))
    
    return redirect("/")
    

if __name__ == '__main__':
    app.run(debug=True)


#set FLASK_APP=app.py
#set FLASK_ENV=development
