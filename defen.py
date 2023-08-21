import os

while True:
        #Input to check if user wants to enter an equation or read from file
    user_choice = input("Pick any to continue; '1' to enter an equation or '2' to read from file or 'q' to quit: ")
        #User chooses to enter an equation
    if user_choice == "1":
        while True:
            try:
                x_input = input("Enter a first number: ")
                y_input = input("Enter a second number: ")
                #Check input are numbers, raise an error if not
                if not (x_input.isnumeric() and y_input.isnumeric()):
                    raise ValueError("Invalid input. Please enter a number")
                x = float(x_input)
                y = float(y_input)
                #Input for operation user wishes to perform 
                operation = input("Enter the operation you wish to perform (+, -, *, /): ")
                #Condition to catch any erros that might occur and error message to 
                #prompt user to enter correct details
                if operation not in ["+", "-", "*", "/"]:
                    raise ValueError("Invalid Input. Please enter a valid operation.")
                #To perform chosen operation and store it in result
                if operation == "+":
                    result =  x + y 
                elif operation == "-":
                    result = x - y 
                elif operation == "*":
                    result = x * y 
                elif operation == "/":
                    result = x / y
                
                print(f"{x} {operation} {y} = {result}")
                #Open the file and write the equation to it
                with open("equation.txt", "a" , encoding="utf-8") as file:
                    file.write(f"{x} {operation} {y} = {result}\n")
                #ask user to enter another equation
                another_eqn = input("Do you want to enter another equation? (yes/no): ")
                if another_eqn.lower() == "no":
                    break
            except ZeroDivisionError:
                print("Cannot divide by zero. Try again")
            except ValueError as error:
                print(error)

    #User chooses to read a file 
    elif user_choice == "2":
        while True:
            #Input to choose file               
            file_name = input("Enter the name of the file you want to read: ")
            #To read file if it exists
            if os.path.isfile(file_name):
                #To read the lines in the text file 
                with open(file_name, "r" , encoding="utf-8") as file:
                    equations = file.readlines()
                #This is meant to strip the file of trailing whitespaces and split into lists
                for i in equations:
                    i = i.strip()
                    parts = i.split()
                    x, operator, y = float(parts[0]), parts[1], float(parts[2])
                    print(i)
                break
            else:
                print("File does not exist. Please enter a valid name")
     #User choosed to exit program   
    elif user_choice == 'q':
        break  #(to break out of the loop after choosing 'q')
    else:
        print("Invalid input. Going back to main menu")
