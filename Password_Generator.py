import random
lst = ("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()")
amount = int(input("How many letters do you want in your password?\n"))
ans = random.choices(lst, k= amount)
password = "".join(ans)
print(password)