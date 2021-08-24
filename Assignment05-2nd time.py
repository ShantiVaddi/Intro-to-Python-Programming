# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoListupdated.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Shanti Vaddi>,<8/23/2021>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoListupdated.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
reader = open(objFile, "r")
for row in reader:
  dicRow = row.split(",")
  dicRow = {"task":dicRow[0].strip(),"priority":dicRow[1].strip()}
  lstTable.append(dicRow)
reader.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        # print(lstTable)
        for dicRow in lstTable:
            print(dicRow["task"] + "," + dicRow["priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strID = input("Enter a task: ")
        strName = input("Enter a priority: ")
        dicRow = {"task": strID, "priority": strName}
        lstTable.append(dicRow)
        print("Added" + strID + "to the list")
        # print(lstTable)
         # for dicRow in lstTable:
            # print(dicRow["task"] + "," + dicRow["priority"])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strID = input("What task you want to delete?: ")
        for dicRow in lstTable:
            if strID == dicRow["task"]:
                lstTable.remove(dicRow)
                print(f"\"{dicRow}\"removed from list.")
                break
        else:
                print(f"\"{dicRow}\"not found.")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif(strChoice.strip() == '4'):
    # Save the data
        writer = open(objFile, "w")
        for dicRow in lstTable:
            writer.write(dicRow["task"] + "," + dicRow["priority"])
        writer.close()
        print("data saved")
        continue
        # TODO: Add Code Here
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
    # TODO: Add Code Here
        print("Thank you for completing the assignment")
    input("\n\nPress the enter key to exit.")
    break
# and Exit the program
