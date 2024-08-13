tasks = []

print("Welcome to To-Do App!")

while True:
    print("\nSelect an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Enter your choice (1:2:3:4): ")

    if choice == '1':
        new_task = input("Enter the task to add: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks added yet.")
        else:
            print("\n---* Tasks *---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to mark as done.")
        else:
            print("\nSelect a task to mark as done:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the task number: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task marked as done!")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
