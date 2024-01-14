todo_list=[]

while True:
    print("===TO Do Application===")
    print("1. Display to do list.")
    print("2 .Add task.")
    print("3 .Remove task.")
    print("4. Quit.")
    choice=input("Enter your choice(1/2/3/4): ")

    if choice=='1':
        print("===TO-Do list===")
        if not todo_list:
            print("No task in the list.")
        else:
            for i in range(len(todo_list)):
                print(f"{i+1}.{todo_list[i]}")
        print("=======================")
    elif choice=='2':
        task=input("Enter the task: ")
        todo_list.append(task)
        print(f"\n'{task}' is added to the To-Do list.")
    elif choice=='3':
        if todo_list:
            index=int(input("Enter the task number to remove: "))
            if 1 <=index <=len(todo_list):
                removed_task=todo_list.pop(index - 1)
                print(f"\n'{removed_task}' has ben removed from the To-Do list.")
            else:
                print("\n Invalid task number.")
        else:
            print("\n No task to removed.")
    elif choice=='4':
        break
    else:
        print("Invalid choice.Please try again.")