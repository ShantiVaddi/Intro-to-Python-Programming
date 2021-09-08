# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <SVaddi>,<09.02.2021>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductobjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <SVaddi>,<09.02.2021>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class(done)
    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # Properties...
    # Product name
    @property
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")
    # Product price
    @property
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price).title()  # Title case

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value): # (setter or mutator)
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise Exception("Price must be numbers! \n\t" + e.__str__().title())

    # -- Methods --
    def __str__(self):
        return self.product_name + ',' + self.product_price


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <SVaddi>,<09.02.2021>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file(done)
    # TODO: Add Code to process data to a file(done)

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ writes data to a file from a list of dictionary rows
        :param file_name : (string) with name of the file
        :param list_of_product_object: (list) of product data saved to file
        :return: (bool) with status of success status
        """

        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_product_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
                raise e
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file from a list into a list of product rows
               :param file_name : (string) with name of the file
               :return: (list of product rows)
               """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
                file.close()
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__, type(e), sep='\n')
            return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO: # TODO: Add docstring(done)
    """ A class performing Input and output
    methods:
        print_menu_items():
        print_current_list_items(list_of_rows):
        input_product_data():
        changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <SVaddi>,<09.02.2021>,Modified code to complete assignment 8:
    """
    # TODO: Add code to show menu to user(done)
    @staticmethod
    def print_menu_items():
        """ print menu of choices to the user """
        print('''
        Menu of Options
        1) show current data
        2) Add a new Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks
    # TODO: Add code to get user's choice(done)
    @staticmethod
    def input_menu_items():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform?[1 to 4]"))
        print() # " Add an extra line for looks"
        return choice

    # TODO: Add code to show the current data from the file to user(done)
    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ print the current items in the list of rows
            :param list_of_rows:(list of rows you want to display
            """
        print("*****  The current products are*****")
        for row in list_of_rows:
            print(row.product_name + "(" + str(row.product_price) + ")")
            print ("******************")
            print() # Add an extra line for looks

        # TODO: Add code to get product data from user(done)
    @staticmethod
    def input_product_data():
        """ Gets data for a product object
        :return: (Product) object with input data
            """
        try:
            name = str(input("What is the product name?").strip())
            price = float(input("What is the price?").strip())
            print() # Add an extra line for looks
            return Product(product_name=name, product_price=price)
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')

    # Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
        # TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
try:
    lstOfProductobjects = FileProcessor.read_data_from_file(strFileName)
    while True:
        # Show user a menu of options
        IO.print_menu_items()
        # Get user's menu option choice
        strChoice = IO.input_menu_items()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.print_current_list_items(lstOfProductobjects)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            lstOfProductobjects.append(IO.input_product_data())
            continue
        elif strChoice.strip() == '3':
            # Let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductobjects)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:

    print("There was an error!Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')

    # let user save current data to file and exit program

