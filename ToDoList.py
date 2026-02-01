# This list will store all tasks added by the user
my_tasks = []

# Display the main menu options
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Get the user's menu choice
    choice = input("Choose an option: ")

    if choice == "1":
# Ask user for a new task and save it in the list
        task = input("Enter a new task: ")
        my_tasks.append(task)
        print("Task added")

    elif choice == "2":
# Show all tasks currently saved
        print("Your Tasks:")
        if len(my_tasks) == 0:
            print("No tasks yet")
        else:
            for pos in range(len(my_tasks)):
                print(pos + 1, my_tasks[pos])

    elif choice == "3":
# Remove a task based on the number selected by the user
        if len(my_tasks) == 0:
            print("Nothing to remove")
        else:
            number = int(input("Enter task number: "))
        if 1 <= number <= len(my_tasks):
                my_tasks.pop(number - 1)
                print("Task removed")
        else:
                print("Invalid number")

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Wrong choice please select again.")
