import requests
from bs4 import BeautifulSoup
from datetime import *
import csv
import json
import os


class Scraping():

    def __init__(self):
        pass


    def get_data(self, company):
        """
        Function to get the share price, percentage movement of the given
        share and date of data retrieval to write on file
        - Share price and percentage taken from yahoo finance webpage

        """
        self.company = company

        self.data = requests.get("https://finance.yahoo.com/quote/" + self.company)

        # Scrapping
        self.soup = BeautifulSoup(self.data.text, "html.parser")

        # Get all the spans
        self.span = self.soup.find_all('span')

        # Get the required spans
        for i in self.span:
            if i['data-reactid'] == "14":
                self.price = i.get_text()
            elif i['data-reactid'] == "16":
                self.percentage = i.get_text()

        # Get the date of the info
        self.get_date = datetime.today()
        self.date = str(self.get_date.day) + "-" + str(self.get_date.month)+ "-" + str(self.get_date.year)

        # Check if both variables have data - used in add_ticker() and remove_ticker()
        try:
            type(self.price)
            type(self.percentage)
        # If not return False
        except:
            return False


    def check_data(self, company):
        """
        Open and check if the date's info is already in the file
        if so change variable self.write to False
        """

        self.company = company

        # Open file and compare dates
        with open('prices.csv') as self.read_file:
            self.read_csv = csv.reader(self.read_file, delimiter=",")
            self.check = " " + self.date
            for row in self.read_csv:
                if self.company == row[0] and self.check == row[3]:
                    self.write = False
        self.read_file.close()


    def write_scrapped_data(self, company):
        """if the date in question is not in the file add all info to csv file else advise"""

        self.company = company

        if self.write:
            self.file = open('prices.csv', 'a')
            self.file.write(self.company + ", " + self.price + ", " + self.percentage + ", " + self.date + "\n")
            self.file.close()
            print(self.company + " data SUCCESFULLY added to " + os.path.basename("prices.csv"))
        else:
            print("Today's information for " + self.company + " has already been processed")
            self.write = True


    def scrape(self):
        """Scrape and write file for multiple tickers"""

        if len(self.companies) < 1:
            print("No companies tracked so far. Please add at least one company ticker to your list")

        elif len(self.companies) > 0:
            for i in self.companies:
                self.get_data(i)
                self.check_data(i)
                self.write_scrapped_data(i)

    def get_tickers(self):

        self.file_name = input("Enter file name EXcluding extension to GET TICKERS:")

        with open(self.file_name + ".json") as self.file:
            self.data = json.load(self.file)
            print(self.data["companies"])

    def add_ticker(self, ticker):
        self.ticker = ticker

        # Check the ticker is valid
        if self.get_data(self.ticker) != False:
            print("HEllO")

            self.file_name = input("Enter file name EXcluding extension to ADD TICKER: ")

            # Check the file to add the ticker is valid
            if os.path.exists(self.file_name + ".json"):

                # Open json file and update with ticker
                with open(self.file_name + ".json") as self.file:
                    self.data = json.load(self.file)
                    # Update json object
                    self.data["companies"].append(self.ticker.upper())
                    self.file.close()

                with open(self.file_name + ".json", "w") as self.file:
                    json.dump(self.data, self.file)

                self.file.close()
                print("Ticker SUCCESFULLY added")

            else:
                print("File does not exist, Please try again")

        else:
            print("Ticker not valid please try again")

    def remove_ticker(self, ticker):
        self.ticker = ticker

        # Check the ticker is valid
        if not self.get_data(self.ticker):

            # Check the file to add the ticker is valid
            if os.path.exists(self.file_name + ".json"):
                self.data = json.load(self.file)
                print(self.data)


        else:
            print("Ticker not valid please try again")



a = Scraping()
a.add_ticker("IPDC.IR")




