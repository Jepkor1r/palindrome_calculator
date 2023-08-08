#!/usr/bin/python3

def perform_palindrome(operator, num1, num2):
    # Function to perform arithmetic operations based on the provided operator
    if operator == '+' :
        return num1 + num2
    elif operator == '-' :
        return num1 - num2 
    elif operator == '*' :
        return num1 * num2 
    elif operator == '/' :
        return num1 / num2 

def calculate_palindrome(result):
    while True:
        user_input = input("Enter something(or 'exit' to quit):")
       
        if user_input.lower() == 'exit':
            print("Exited successfully.")
            break
        try:
         # Remove spaces from user input to handle palindromes with spaces
         user_input_no_spaces = "".join(user_input.split())
         # Get the first number from the user
         num1 = int(input("Enter the first number:"))
         # Get the arithmetic operator from the user
         operator = input("Enter arithmetic operator(+, -, *, /):")
         # Get the second number from the user
         num2 = int(input("Enter the second number:"))
         # Perform the arithmetic operation and store the result
         result = perform_palindrome(operator, num1, num2)
         # Convert the result to a string before performing the palindrome check
         result_string = str(result)
       
        except ValueError:
           # Handle invalid input for numbers   
            print("Wrong input. Palindrome check skipped.")
        # Check if the original user input is a palindrome   
        if user_input == user_input[::-1]: #Slicing user_input in reverse order with step -1.
           print("Yes, '{}' is a palindrome.".format(user_input))
        else:
          print("Oops!, '{}' is not a palindrome.".format(user_input))
        # Check if the user input without spaces is a palindrome  
        if user_input_no_spaces == user_input_no_spaces[::-1]:
          print("Congratulations! '{}' is a palindrome.".format(user_input_no_spaces))
        else:
          print("Try again!, '{}' is not a palindrome.".format(user_input_no_spaces))
        # Check if the result of the arithmetic operation is a palindrome  
        if result_string == result_string[::-1]:
            print("'{}' is a palindrome. You awesome!".format(result_string))
        else:
            print("'{}' is not a palindrome. You got this!".format(result_string))

# Start the palindrome checking and arithmetic calculation loop
calculate_palindrome(perform_palindrome)
