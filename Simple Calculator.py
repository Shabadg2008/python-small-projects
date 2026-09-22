from math import *
while True:
    question = input("Enter your problem:\n")
    ans = eval(question)
    print (round(ans, 2))
    another = input("Do you have another problem? Yes/No\n")
    if another == "No":
        break
    
                  
            