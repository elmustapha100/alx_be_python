# Multiplication Table Generator 

number = int(input("Enter a number  to see its multiplication table: ")) 

for Y  in range(1, 11) :
    Z = number * Y
    # printing the result in the format X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.
    print(f"{number} * {Y} = {Z}")



