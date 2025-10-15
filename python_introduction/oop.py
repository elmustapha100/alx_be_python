#class methods and static methods

class Food : 
    count = 0 #Creating a count variable as the class Food variable 

    def __init__(self,food_name) : 
        self.food_name = food_name 
        Food.count += 1 

    @classmethod 
    def display_food_count(cls) : #Note while defining a method in OOP , the paramter is self . Notice that change 
                                #in the class method , the parameter conventionally is cls referring to the class
        print(f"Total food available is {cls.count}")

#Class Instances

food_1 = Food("Rice")
food_2 = Food("Spaghetti")

Food.display_food_count() 

#Static method : 
#A method in a class that is independent of any instance of that class , i.e it can be created
#without creating an instance(object) of the class 

class Math : 
    @staticmethod 

    def add(a,b): 
        return a + b 
    
    @staticmethod 
    def multiply(a,b): 
        return a * b 
    
print(Math.add(2,8))
print(Math.multiply(90,65))    