from datetime import date, datetime, timedelta

def  display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)
    while True:
        try:
            future_date = int(input("Enter your number of days: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    def calculate_future_date(future_date):
         future = current_date + timedelta(days=future_date)
         return future.strftime("%Y-%m-%d")
    print(f"Future date after {future_date} days is: {calculate_future_date(future_date)}")
    
display_current_datetime()