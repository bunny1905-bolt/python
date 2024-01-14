# ToDo List Application using Lists and Dictionaries

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    print("\n===== ToDo List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task_name = input("Enter the task: ")
    task_priority = input("Enter the priority (High/Medium/Low): ")

    task = {"Name": task_name, "Priority": task_priority, "Completed": False}
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("\n===== Task List =====")
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['Name']} - Priority: {task['Priority']} - Completed: {task['Completed']}")

def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["Completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task['Name']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting ToDo List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")