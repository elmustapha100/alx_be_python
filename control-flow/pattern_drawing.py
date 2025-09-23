#  Drawing Patterns with Nested Loops using asteriks 

size  = int(input("Enter the size of the pattern : ")) 

#using while loop to iterate the rows 
rows = 0 

while rows < size : 
    #using for loop to iterate the columns 
    for i in range(size) : 
        print("*" , end="")

    print() # to move to the next line 

    rows += 1     

