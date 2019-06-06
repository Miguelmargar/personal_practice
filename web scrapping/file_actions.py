import os


class file():

    def __init__(self):

        self.write = True

    def create_file(self):
        """
        Create a new csv file in directory
        Checks whether the file already exists or not
        """

        # Check if the file exists already if so advise
        try:
            self.already = True

            while self.already:

                # Ask user for new csv file name wanted
                self.file_name = input("Enter file name to CREATE FILE INcluding extension: ")

                if open(self.file_name, 'r'):
                    print("File name already exits, please select a new one")

        # If file does not exist already create it
        except:
            self.new_file = open(self.file_name, 'w+')
            print("xxxxxxxx FILE CREATED xxxxxxxx")
            self.new_file.close()


    def write_csv_headers(self):
        """Write on an empty csv file the desired headers"""

        self.exists = True

        while self.exists:

            # Ask user for wanted file to write on
            self.file_name = input("Enter file name to INPUT HEADERS INcluding extension: ")

            try:
                with open(self.file_name, "w") as self.read_file:
                    # If the file is empty
                    if os.path.getsize(self.file_name) == 0:
                        self.header = input("Please type the domain names: ")
                        self.read_file.write(self.header + "\n")
                        print("xxxxxxxx HEADERS ADDED xxxxxxxx")

                    # If the file is not empty advise
                    else:
                        print("File is not empty")

                self.read_file.close()
                self.exists = False

            except:
                print("File does not exist, please check spelling and try again")


    def print_csv_contents(self):
        """
        Print all the file contents
        Check to see if file exists
        """
        # Assume file does not exists
        self.exists = True

        # As long as it doesn't exist
        while self.exists:

            # Ask user for wanted file to print
            self.file_name = input("Enter file name to PRINT contents INcluding extension: ")

            try:
                # Open the required file print it out and close file
                with open(self.file_name) as self.read_file:
                    for line in self.read_file:
                        print(line, end = " ")
                self.read_file.close()
                self.exists = False

            except:
                # Inform the user the file name given does not exist
                print("File does not exist, please check spelling and try again")


    def exists_csv(self):
        """Check if file exists"""

        # Ask user for wanted file to check
        self.file_name = input("Enter file name to CHECK INcluding extension: ")

        if os.path.exists(self.file_name):
            print("xxxxxxxx FILE EXISTS xxxxxxxx")
        else:
            print("xxxxxxxx FILE DOES NOT EXIST xxxxxxxx")



