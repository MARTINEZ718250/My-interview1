while True:
    
    input_string = input("Enter numbers separated by commas (e.g., 1,2,3,4) or type 'exit' to quit: ")
    
  
    if input_string.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
       
        numbers = [int(num) for num in input_string.split(',')]
        
       
        total_sum = 0
        
       
        for number in numbers:
            total_sum += number  
        
       
        print("The sum of the numbers you entered is:", total_sum)
    
    except ValueError:
        print("Please enter valid numbers separated by commas.")

#Explanation
#While Loop: The while True loop keeps the program running until the user decides to exit.
#User Input: The program prompts the user to enter numbers or type 'exit' to quit.
#Exit Condition: If the user types 'exit', the program prints a message and breaks out of the loop, ending the program.
#Try-Except Block: The try block attempts to process the user input. If there's an error (e.g., non-numeric input), the except block handles it by informing the user.
#Processing Input: If the input is valid, it's split into integers, summed, and the result is printed.
#This approach provides a user-friendly way to repeatedly perform calculations and handle invalid input easily.





