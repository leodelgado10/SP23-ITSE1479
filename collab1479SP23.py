# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2023";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Becker - call to function goes here
    jumpTable['3'] = stub                 # Cantu - call to function goes here
    jumpTable['4'] = delgadoFunction                 # Delgado - call to function goes here
    jumpTable['5'] = stub                 # Garcia Tadeo - call to function goes here
    jumpTable['6'] = stub                 # Gloria - call to function goes here
    jumpTable['7'] = stub                 # Menifee - call to function goes here
    jumpTable['8'] = stub                 # Rountree - call to function goes here
    jumpTable['9'] = stub                 # Stewart - call to function goes here
    jumpTable['10'] = stub                # Sylvester - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Becker")
    print("3.  Cantu")
    print("4.  Delgado")
    print("5.  Garcia Tadeo")
    print("6.  Gloria")
    print("7.  Menifee")
    print("8.  Rountree")
    print("9.  Stewart")
    print("10. Sylvester")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************
def delgadoFunction():
    delgadoPassword()
    print()
    print("Press ENTER to return to the menu")
    input()
def delgadoPassword():
    lastName = input("Please enter your last name")
    birthCity = input("Please enter your birth city")
    phoneNumber = input("Please enter your phone number, numbers only and no dashes: ")

    reversedLastName = lastName[::-1][:4]

    #will determine what to use from city of birth 
    if birthCity[0].lower() in "aeiou":
        cityChar = ":"
    elif birthCity[0].lower() in "abcdefghijklm":
        cityChar = ";"
    else:
        cityChar = "!"

    #Making paswword from phone number  
    phoneSum = sum(int(num) for num in phoneNumber)

    passwordNum = ((phoneSum/7) * 63)

    #combining all components 
    password = f"{reversedLastName}{cityChar}{int(passwordNum)}"

    print("***********************************")
    print("* Strong Password Program")
    print("***********************************\n")
    print("Enter the following information")
    print("-------------------------------")
    print("Last Name: ", lastName)
    print("Birth City: ", birthCity)
    print("Phone Number (number only): ", phoneNumber)
    print()
    print(f"Your strong password is: {str(password)}")
# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
