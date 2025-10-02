# Temperature Conversion Tool 

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celsius(fahrenheit) : 
    """converts fahrenheit to celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius) :
    """converts celsius to fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
def main(): 
    try:
        temperature = float(input("Enter the temperature to convert: "))
        temp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Based on the user input, conditions to be checked
        if temp_scale == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif temp_scale == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid temperature. Please enter a numeric value.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()