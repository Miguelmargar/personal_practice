import requests
from bs4 import BeautifulSoup
from datetime import *
import csv
import os

class scraping():

    def __init__(self):

        self.write = True

        # Companies tickers
        self.companies = ["BIRG.IR"]


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


    def check_data(self):
        """
        Open and check if the date's info is already in the file
        if so change variable self.write to False
        """
        # Open file and compare dates
        with open('prices.csv') as self.read_file:
            self.read_csv = csv.reader(self.read_file, delimiter=",")
            self.check = " " + self.date
            for row in self.read_csv:
                if self.check == row[3]:
                    self.write = False
        self.read_file.close()


    def write_scrapped_data(self):
        """if the date in question is not in the file add all info to csv file else advise"""

        if len(self.company) < 1:
            print("Please add a company ticker to your list of companies")

        elif len(self.company) > 0:
            if self.write:

                self.file = open('prices.csv', 'a')
                self.file.write(self.company[i] + ", " + self.price + ", " + self.percentage + ", " + self.date + "\n")
                self.file.close()
                print("Data SUCCESFULLY added to " + os.path.basename("prices.csv"))
            else:
                print("Today's information has already been processed")


    def scrape(self):
        """Scrape and write file for multiple tickers"""

        for i in self.companies:
            self.get_data()
            self.check_data()
            self.write_scrapped_data()








    def create_csv_file(self):
        """
        Create a new csv file in directory
        Checks whether the file already exists or not
        """

        # Check if the file exists already if so advise
        try:
            self.already = True

            while self.already:

                # Ask user for new csv file name wanted
                self.file_name = input("Enter file name to CREATE FILE EXcluding extension: ")

                if open(self.file_name + ".csv", 'r'):
                    print("File name already exits, please select a new one")

        # If file does not exist already create it
        except:
            self.new_file = open(self.file_name + ".csv", 'w+')
            print("xxxxxxxx FILE CREATED xxxxxxxx")
            self.new_file.close()


    def write_csv_headers(self):
        """Write on an empty csv file the desired headers"""

        self.exists = True

        while self.exists:

            # Ask user for wanted file to write on
            self.file_name = input("Enter file name to INPUT HEADERS EXcluding extension: ")

            try:
                with open(self.file_name + ".csv", "w") as self.read_file:
                    # If the file is empty
                    if os.path.getsize(self.file_name + ".csv") == 0:
                        self.header = input("Please type the domain names: ")
                        self.read_file.write(self.header + "\n")
                        print("xxxxxxxx HEADERS ADDED xxxxxxxx")

                    # If the file is not empty advise
                    else:
                        print("File is not empty")

                self.read_file.close()
                self.exists = False

            except:
                print("File name does not exist, please check spelling and try again")


    def print_contents(self):
        """
        Print all the file contents
        Check to see if file exists
        """
        # Assume file does not exists
        self.exists = True

        # As long as it doesn't exist
        while self.exists:

            # Ask user for wanted file to print
            self.file_name = input("Enter file name to PRINT contents EXcluding extension: ")

            try:
                # Open the required file print it out and close file
                with open(self.file_name + ".csv") as self.read_file:
                    for line in self.read_file:
                        print(line, end = " ")
                self.read_file.close()
                self.exists = False

            except:
                # Inform the user the file name given does not exist
                print("File name does not exist, please check spelling and try again")


    def exists(self):
        """Check if file exists"""

        # Ask user for wanted file to check
        self.file_name = input("Enter file name to CHECK EXcluding extension: ")

        if os.path.exists(self.file_name + ".csv"):
            print("xxxxxxxx FILE EXISTS xxxxxxxx")
        else:
            print("xxxxxxxx FILE DOES NOT EXIST xxxxxxxx")


a = scraping()
# a.scrape()




# Tested and working:
# a.create_csv_file()
# a.write_csv_headers()
# a.print_contents()
# a.exists()
