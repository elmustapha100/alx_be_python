# Arithmetic Operations Function

def perform_operation(num1, num2, operation): 
    """A function that performs arithmetic operations ontwo numerical values."""

    if operation == "add" : 
        return num1 + num2 
    
    elif operation == "subtract" :
        return num1 - num2 
    
    elif operation == "multiply" : 
        return num1 * num2 
    
    elif operation == "divide" : 
        if num2 == 0 : 
         return "Error: Cannot divide by zero"
        else : 
          return num1 / num2
     
    else :
        return "Error: Invalid operation" 

    