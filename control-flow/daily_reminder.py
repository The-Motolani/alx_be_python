task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound =input("Is it time-bound? (yes/no): ").lower()
match priority:
   case "high" if time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
   case "high" if time_bound == "no":
    print(f"Reminder: '{task}' is a high priority test. Do it before the day ends.")
   case "medium" if time_bound == "yes":
    print(f"Reminder: '{task} is a medium priority task but is also time bound and requires you to get started on it.'")
   case "medium" if  time_bound == "no":
    print(f"Note: '{task}' is a medium priority task. Consider starting on it.")
   case "low":
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
   case _:
    print("Invalid input")