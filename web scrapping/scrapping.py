import requests
from bs4 import BeautifulSoup



data = requests.get("https://finance.yahoo.com/quote/BIRG.IR?p=BIRG.IR")

soup = BeautifulSoup(data.text, "html.parser")

span = soup.find_all('span')

for i in span:
    if i['data-reactid'] == "14" or i['data-reactid'] == "16":
        print(i.get_text())
                
