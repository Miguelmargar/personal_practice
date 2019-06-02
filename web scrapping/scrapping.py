import requests
from bs4 import BeautifulSoup
from datetime import *
from time import sleep


def getInfo():
    """
    Function to get the share price, percentage movement of the given
    share and date of data retrieval to write on file
    - Share price and percentage taken from yahoo finance webpage

    """
    # Company share price ticker
    company = "BIRG.IR"

    # yahoo finance page
    data = requests.get("https://finance.yahoo.com/quote/" + company)

    # Scrapping 
    soup = BeautifulSoup(data.text, "html.parser")

    # Get all the spans
    span = soup.find_all('span')

    # Get the required spans
    for i in span:
        if i['data-reactid'] == "14":
            price = i.get_text()

        elif i['data-reactid'] == "16":
            percentage = i.get_text()

    # Get the date of the info
    getDate = datetime.today()     
    date = str(getDate.day) + "-" + str(getDate.month)+ "-" + str(getDate.year)

    # Open file, write the required date and close file
    file = open('prices.csv', 'a')
    file.write(price + ", " + percentage + ", " + date + "\n")
    file.close()

getInfo()




