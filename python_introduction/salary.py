#This program is practice program on OOP that checks the raise in salary for a set of employers 

class Workers: 
    # num_of_employers = 0
    raise_in_salary = 0

    def __init__(self,first_name,last_name,pay): 
        self.first_name = first_name
        self.last_name = last_name 
        self.email = (first_name + '.' + last_name[0:4] + '@gmail.com').strip().lower()
        self.pay = pay 

    #Getting user's fullname and email
    def full_name(self): 
        return f"{self.first_name} {self.last_name}\n{self.email}"
    
    #Increase in salary 
    #In a system,e.g a startup company where there sre different % of increment according to the role in the company 

    try : 
        def position(self):
            work_position = input("What is your position in the organisation : ")

            if work_position == "Frontend Developer" : 
                Workers.raise_in_salary += 0.5 
                new_payment = int(self.pay * Workers.raise_in_salary)
                final_pay = self.pay + new_payment
                print(f"Acording to your role , your monthly payment has been increased to ${final_pay}")

            elif work_position == "Backend Developer" : 
                Workers.raise_in_salary += 0.8
                new_payment = int(self.pay * Workers.raise_in_salary)
                final_pay = self.pay + new_payment
                print(f"Acording to your role , your monthly payment has been increased to ${final_pay}")

            elif work_position == "UI/UX Designer" : 
                Workers.raise_in_salary += 0.7
                new_payment = int(self.pay * Workers.raise_in_salary)
                final_pay = self.pay + new_payment
                print(f"Acording to your role , your monthly payment has been increased to ${final_pay}")   

            elif work_position == "Product Manager" : 
                Workers.raise_in_salary += 0.55
                new_payment = int(self.pay * Workers.raise_in_salary)
                final_pay = self.pay + new_payment
                print(f"Acording to your role , your monthly payment has been increased to ${final_pay}") 
            else : 
                print(f"You are not eligible for the increase in salary!!!")   

    except Exception as e : 
        print(f'{e}. Enter a valid position as required by the startup')                  

worker = Workers("Mustapha" , "Abimbola", 1500) 
print(f"Hello {worker.full_name()} ")    
print(worker.position())     


