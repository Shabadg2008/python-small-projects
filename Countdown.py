from datetime import datetime
Ans = input("What date would you like to countdown to? \n")
Countdown_Date = datetime.strptime(Ans, "%m/%d/%Y")
Current_Date = datetime.now()
Remaining_Time = Countdown_Date - Current_Date
print(f"Remaining time: {Countdown_Date - Current_Date}")
