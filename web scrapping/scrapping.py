import requests
from bs4 import BeautifulSoup
from datetime import *
import csv

class scraping():

    def __init__(self):
        pass

    def get_data(self):
        """
        Function to get the share price, percentage movement of the given
        share and date of data retrieval to write on file
        - Share price and percentage taken from yahoo finance webpage

        """
        # Company share price ticker
        self.company = "BIRG.IR"

        # yahoo finance page
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

        with open('prices.csv') as self.read_file:
            self.read_csv = csv.reader(self.read_file, delimiter=",")
            self.check = " " + self.date
            for row in self.read_csv:
                if self.check == row[2]:
                    self.write = False
        self.readFile.close()


    def write_scrapped_data(self):
        """if the date in question is not in the file add all info to csv file else advise"""

        self.write = True

        if self.write:
            self.file = open('prices.csv', 'a')
            self.file.write(self.price + ", " + self.percentage + ", " + self.date + "\n")
            self.file.close()
        else:
            print("Today's information has already been processed")


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
                self.file_name = input("Enter file name including extension: ")

                if open(self.file_name + ".csv", 'r'):
                    print("File name already exits, please select a new one")

        # If file does not exist already create it
        except:
            self.new_file = open(self.file_name + ".csv", 'w+')
            self.new_file.close()


    def write_csv_headers(self):
        """Write on the csv file desired headers"""


    def print_contents(self):
        """Print all the file contents"""
        # Assume file does not exists
        self.exists = True

        # As long as it doesn't exist
        while self.exists:
            # Ask user for wanted file to print
            self.file_name = input("Enter file name including extension: ")

            try:
                # Open the required file and print it out
                with open(self.file_name) as self.read_file:
                    for line in self.read_file:
                        print(line, end = " ")
                self.exists = False

            except:

                print("File name does not exist, please check spelling and try again")








# a = scraping()
# a.get_data()
# a.check_data()
# a.write_scrapped_data()

# Tested and working:
# a.create_csv_file()
# a.print_contents()

