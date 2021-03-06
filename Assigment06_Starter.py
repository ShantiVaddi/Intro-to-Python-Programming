# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# <Shanti Vaddi>,<08/24/2021>,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoList.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list_of_dictionaries(list_of_dictionary_rows, task, priority):
        """ Adds data to a list of dictionary rows

                :param list_of_dictionary_rows:: (string) with name of file:
                :param task: (string) with name of task
                :return: priority: (string) with name of priority
                """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        list_of_dictionary_rows.append(row)

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes a row of data from a list of dictionary rows
        :param list_of_dictionary_rows: (list) of dictionary data to remove a row from
        :param task_to_remove: (string) with name of the task in the dictionary's 'Task' key
        :return: (list) list_of_dictionary_rows, (bool) with status of success status"""
        success_status = False  # Create a boolean Flag for loop
        row_number = 0  # Create a counter to identify the current dictionary row in the loop
        # Search though the table or rows for a 'Task' key match
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                list_of_rows.remove(row)
                # print("row removed")
                success_status = True
                row_number += 1
        return list_of_rows, success_status

        # TODO: Add Code Here!

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        file = open(file_name, "w")
        for dicRow in list_of_rows:
            file.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        file.close()
        success_status = True
        return success_status
        # TODO: Add Code Here!

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit ProgramA
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        task = input("Enter a task name")
        priority = input("Enter the priority")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        task = input("You want to remove the task")
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task,priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list_of_dictionaries(lstTable,task,priority)
        # TODO: Add Code Here
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        Processor.remove_data_from_list(task,lstTable)
        # TODO: Add Code Here
        IO.input_press_to_continue(strStatus)

        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        # IO.print_menu_Tasks():
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName,lstTable)
            IO.print_menu_Tasks()
            input("Data saved to file!")
        else:
            input("New data was NOT Saved, but previous data still exists")

        # TODO: Add Code Here!
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable.clear()
            Processor.read_data_from_file(strFileName, lstTable)
            IO.print_menu_Tasks()
            # TODO: Add Code Here!

        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit