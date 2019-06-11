import requests
from bs4 import BeautifulSoup
from datetime import *
import csv
import json
import os
import re 


class Scraping:

    def __init__(self):

        self.write = True

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

        # Regex for checking price and percentage pattern to be correct
        self.reg_price = re.compile("^([0-9|.]*)")
        self.reg_percentage = re.compile("^([+|-])([0-9|.]*)(\s)(\(([+|-])([0-9|.]*)\%\))")

        # Get the required spans
        for i in self.span:
            if i['data-reactid'] == "14" and self.reg_price.match(i.get_text()) is not None:
                self.price = i.get_text()

            elif i['data-reactid'] == "16" and self.reg_percentage.match(i.get_text()):
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

        with open("companies.json") as self.file:
            self.data = json.load(self.file)
        self.file.close()

        if len(self.data["companies"]) < 1:
            print("No companies tracked so far. Please add at least one company ticker to your list")

        elif len(self.data["companies"]) > 0:
            for i in self.data["companies"]:
                self.get_data(i)
                self.check_data(i)
                self.write_scrapped_data(i)


    def get_tickers(self):
        """Get all the tickers being followed"""

        with open("companies.json") as self.file:
            self.data = json.load(self.file)
            return self.data["companies"]


    def get_first_ticker(self):
        """Get the 1st ticker in list only"""

        with open('prices.csv') as self.read_file:
            self.read_csv = csv.reader(self.read_file, delimiter=",")
            for i, row in enumerate(self.read_csv):
                if i == 1:
                    return row
        self.read_file.close()


    def add_ticker(self, ticker):
        """
        Add ticker function
        Check if ticker is valid, already in list and if file exists
        """

        self.ticker = ticker

        # Check the ticker is valid
        if self.get_data(self.ticker) != False:

            self.file_name = input("Enter file name EXcluding extension to ADD Ticker: ")

            # Check the file to add the ticker is valid
            if os.path.exists(self.file_name + ".json"):

                # Open json file and update with ticker
                with open(self.file_name + ".json") as self.file:
                    self.data = json.load(self.file)

                    # Check the ticker is not already in the list
                    if self.ticker not in self.data["companies"]:
                        # Update json object
                        self.data["companies"].append(self.ticker.upper())
                        self.file.close()

                        with open(self.file_name + ".json", "w") as self.file:
                            json.dump(self.data, self.file)
                        self.file.close()
                        print("Ticker SUCCESFULLY added")
                    else:
                        print("Ticker is already in the list")

            else:
                print("File does not exist, Please try again")

        else:
            print("Ticker not valid please try again")


    def remove_ticker(self, ticker):
        self.ticker = ticker

        self.file_name = input("Enter file name EXcluding extension to REMOVE Ticker: ")

        # Check the file to add the ticker is valid
        if os.path.exists(self.file_name + ".json"):

            with open(self.file_name + ".json") as self.file:
                self.data = json.load(self.file)
                if self.ticker in self.data["companies"]:
                    self.data["companies"].remove(self.ticker)
                    self.file.close()

                    with open(self.file_name + ".json", "w") as self.file:
                        json.dump(self.data, self.file)
                    self.file.close()
                    print("Ticker Succesfully removed")

                else:
                    print("Ticker was not in the list")

        else:
            print("File does not exist")


a = Scraping()
a.scrape()


