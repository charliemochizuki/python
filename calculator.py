c = "\x1bc"  #clear console screen variable
print(c)  #to clear the console

#Header
print(71*"=")
print("\t\t\tPython's Basic Calculator")
print(71*"=")
print("Use these Operation Symbols to operate the calculations [+] [-] [*] [/]\n")

#create functions for multiple operations like (add, substract, multiply and divide)
def add (a,b):
    return a + b
def substract (a,b):
    return a - b
def multiply (a,b):
    return a * b
def divide (a,b):
    return a / b

#create library to run the functions when the symbol is chosen
operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Enter the number\t:   ")) #ask the user to enter the first numbers 
again = True  # create again (variable) and mark the value as True
while again:   #While again = while True
    operation_symbol = input("Type of operation\t: ")   #-- create new variable (operation_symbol) to choose the operation 
    calculation = operation[operation_symbol]   #-- create ne variable (calculation) to activate the library according to the symbol chosen
    num2 = int(input("The next number\t\t:   "))   #-- create variable for the next numbers
    result = calculation (num1,num2)    #create variable (result) to activate the calculation (variable) with the input of num1 and num2
    print(f"\t\tResult\t: {num1} {operation_symbol} {num2} = {result}\n")   #-- print the variable of num1, operation_symbol, num2 and result using f-string
    if input("Type [Y] if you wish to continue the operations, or any key  or just ENTER to exit! ").lower() == "y":   #-- create if function with input to choose to continue or exit
        num1 = result   #-- if "Y" is chosen, then the value of num1 is the value of result. To continue the value for the next operation
        print(f"Previous number\t\t:    {result}")  #-- print out the result's value as the the first number (num1) to continue the operations
    else:      #-- if the choice is not "Y" 
        again = False    #-- again = False. this will stop the while loop
        print("Thank you and see you again!\n")  #-- while loop is stopped, print out thank you to appreciate the users
        print()   # To print the blak row as the project is exited 

