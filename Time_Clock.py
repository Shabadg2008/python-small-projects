import time 
time_counted = int(input("Set your alarm (sec): \n"))
countdown = time_counted
while countdown > 0:
    print(f"Your time remaining is {countdown} seconds")
    time.sleep(1)
    countdown -=1
print("Time's Up!")