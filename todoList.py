print("PENDING TASKS\n")

# Initial task list
taskList = ["homework", "groceries", "walk dog", "vacuum", "laundry", "wash car"]

# Display the initial tasks
print("Current tasks:", taskList, '\n')

# Create a loop to allow the user to manage tasks until they choose to quit
while True:
    # Ask the user what they want to do
    userPath = input("What would you like to do? (Remove completed task(1), Add a new task(2), or Quit(3)): \n")

    if userPath == "1":
        completedTask = input("Have you completed a task? (Yes/No): ").lower()
        if completedTask == "yes":
            print("Here are your current tasks:\n", taskList, '\n')
            completedTask = input("What task have you completed? (Pick from list): \n")

            if completedTask in taskList:
                # Find the index and remove the task
                taskIndex = taskList.index(completedTask)
                taskList.pop(taskIndex)
                print(f"Task '{completedTask}' has been completed and removed from the list.")
                print("Updated task list:\n", taskList)
            else:
                print(f"Task '{completedTask}' not found in the list.")
        else:
            print("No task was completed.")

    elif userPath == "2":
        # Add a new task
        while True:
            newListItem = input("Name of the task you want to add to the TODO list: \n")
            if newListItem not in taskList:
                taskList.append(newListItem)
                print(f"You've added '{newListItem}' to the task list.\n")
            else:
                print(f"Task '{newListItem}' is already in the list.")

            # Ask if the user wants to add another task
            anotherTask = input("Would you like to add another item to the TODO list? (Yes/No): \n").lower()
            if anotherTask != "yes":
                break

    elif userPath == "3":
        # Quit the program
        print("Exiting the to-do list.")
        break

    else:
        print("Invalid input. Please try again.")

    # Display the current number of tasks
    print(f"You currently have {len(taskList)} tasks.\n")

print("Final task list:", taskList)
