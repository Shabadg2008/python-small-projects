from datetime import datetime
Ans = input("What date would you like to countdown to? mm/dd/yr \n")
Countdown_Date = datetime.strptime(Ans, "%m/%d/%Y")
Current_Date = datetime.now()
Remaining_Time = Countdown_Date - Current_Date
Total_sec = Remaining_Time.total_seconds()
print(f"Remaining Years: {round(Remaining_Time.days / 365, 2)}")
print(f"Remaining Months: {round(Remaining_Time.days / 30.44, 1)}")
print(f"Remaining Days: {round(Remaining_Time.days)}")
print(f"Remaining Hours: {round(Total_sec / 3600, 1)}")
print(f"Remaining Minutes: {round(Total_sec / 60, 1)}")
print(f"Remaining Seconds: {round(Total_sec)}")
