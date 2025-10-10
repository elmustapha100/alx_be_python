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
     return f"Error: Cannot divide by zero."  
    except ValueError : 
       return f"Error: Please enter numeric values only."