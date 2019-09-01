### This Program for simulate a simple Calculator
### © Created By Me.
while True:
    print("\n\n-----************-----   Options Below\/\/  -----************-----")
    print("\n     :: Enter 'add' to add two numbers.")
    print("\n     :: Enter 'subtract' to subtract two numbers.")
    print("\n     :: Enter 'multiply' to multiply two numbers.")
    print("\n     :: Enter 'divide' to divide two numbers.")
    print("\n     :: Enter 'quit' to end the program.")

    print(" \n    [!][!] Choose one option from the options listed above.")
    user_input = input("     What operation do you need? ")
    if user_input == "quit":
        break

    num1 = input(" \nEnter the first number : ")
    num2 = input(" \nEnter the second number : ")
    if user_input == "add":
        print(" \nTwo numbers have been added successfully. \n                                  ",num1," + ",num2," = ",int(num1)+int(num2))
    elif user_input == "subtract":
        print(" \nTwo numbers have been subtract successfully. \n                               %c - %c = %d" %(num1,num2,int(num1)-int(num2)))
    elif user_input == "multiply":
        print(" \nTwo numbers have been multiply successfully. \n                               %c * %c = %d" %(num1,num2,int(num1)*int(num2)))
    elif user_input == "divide":
        print(" \nTwo numbers have been divided successfully. \n                                %s / %s = %.2f" %(num1,num2,float(num1)/float(num2)))

    user_input = input("  \nEnter 'quit' if you want ? ")
    if user_input == "quit":
        break

    ## The end, until be improved in the next days ... Insha'ALLAH