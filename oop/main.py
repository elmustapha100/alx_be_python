from class_static_methods_demo import Calculator 

#Implementing the static method 
def main() : 
    sum_result = Calculator.add(10,5)
    print(f"The sum is: {sum_result}")
    
    #Implementing the class method 

    product_result = Calculator.multiply(10,5)
    print(f"The product is: {product_result}")

if __name__ == "__main__" : 
    main() 

 