##

def safe_divide(numerator, denominator): 
    """This function performs division, handling potential errors"""
    try : 
        num = float(numerator)
        denum = float(denominator)
        #Attempting division cautious with errors 
        result = num/denum 
        return f"The result of the division is {result}"
            
    except ZeroDivisionError : 
     print(f"Error: Cannot divide by zero.")  
    except ValueError : 
       print(f"Error: Please enter numeric values only.")