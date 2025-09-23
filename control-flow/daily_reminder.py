# Program Objective: Create a simplified Python script that uses conditional statements,
# Match Case, and loops to remind the user about a single,
# priority task for the day based on time sensitivity.

task = input("Enter your task  : ")
priority = input("priority (high/medium/low):  ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority : 
    case "high" : 
        if time_bound == "yes" : 
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else : 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

    case "medium" : 
        print(f"'{task}' is a medium priority task. ")        

    case "low" : 
        if time_bound == "yes" : 
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today! .")
        else : 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time. ")   

    case _ : 
        print(f"'{task}' is a task with unrecognized priority level")
