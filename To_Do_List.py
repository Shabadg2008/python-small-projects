Tasks = []
while True:
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    choice = input("Pick what you want to do, 1-4\n")
    if choice == "2":
        add = input("What task do you want to add?\n")
        Tasks.append(add)
        print("Your tasks are:", Tasks)
    elif choice == "3":
        rem = input("What task do you want to remove?\n")
        if rem in Tasks:
            Tasks.remove(rem)
            print("Your tasks are:", Tasks)
        else:
            print("Task not found")
    elif choice == "1":
        print(Tasks)
    elif choice == "4":
        print("Bye")
        break
    