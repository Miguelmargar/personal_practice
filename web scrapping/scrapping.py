import requests
from bs4 import BeautifulSoup



def getInfo():
    """
    Function to get the share price and percentage movement of the given
    share - taken from yahoo finance webpage

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
        if i['data-reactid'] == "14" or i['data-reactid'] == "16":
            print(i.get_text())
                

getInfo()
