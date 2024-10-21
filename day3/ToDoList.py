def start():
    # Initialize an empty list to store tasks
    todo_list = []

    # Infinite loop to keep the program running until the user decides to exit
    while True:
        # Display the title "To Do List" centered on the screen
        print("\n\n")
        print("To Do List".center(80))
        print("\n\n\t 1. Add Task")
        print("\t 2. Remove Task")
        print("\t 3. Update Task")
        print("\t 4. See All Tasks")
        print("\t 5. Exit")

        # Ask the user for their choice
        ch = input("\n\n\t Enter Your Choice: ")

        # Use match-case to handle different choices
        match ch:
            case '1':
                # Option to add tasks
                n_task = input("\n\n\t Enter How Many Tasks You Want to Add: ")

                # Loop to add the specified number of tasks
                for i in range(1, (int(n_task) + 1)):
                    v_task = input(f"\n\n\t Enter Task {i}: ")
                    todo_list.append(v_task)  # Append each task to the list

                print("\n\t Tasks Added Successfully")

            case '2':
                # Option to remove a specific task
                r_task = input("\n\n\t Enter the Task You Want to Remove: ")

                # Check if the task exists in the list, and remove it if found
                if r_task in todo_list:
                    todo_list.remove(r_task)
                    print(f"\n\t {r_task} Task Removed Successfully")
                else:
                    # If the task is not found, display a message
                    print(f"\n\t {r_task} Task Not Found!!")

            case '3':
                # Option to update a specific task
                u_task = input("\n\n\t Enter the Task You Want to Update: ")

                # Check if the task exists in the list
                if u_task in todo_list:
                    list_index = todo_list.index(u_task)  # Get the index of the task
                    up_task = input("\n\n\t Enter Updated Task: ")
                    todo_list.insert(list_index, up_task)  # Insert the updated task at the same index
                    todo_list.remove(u_task)  # Remove the old task
                    print(f"\n\t {u_task} Task was Replaced by {up_task} Task")
                else:
                    # If the task is not found, display a message
                    print(f"\n\t {u_task} Task was Not Found in To Do List")

            case '4':
                # Option to view all tasks in the to-do list
                if len(todo_list) <= 0:
                    # If the list is empty, display a message
                    print("\n\n\t To Do List is Empty")
                else:
                    # Display all tasks with their index numbers
                    print("\n\n")
                    print("To Do List".center(80))
                    for i in range(0, len(todo_list)):
                        print(f"\n\n\t {i+1}. {todo_list[i]}")

            case '5':
                # Exit the program
                break

            case _:
                # Default case for invalid input
                print("\n\n\t Please Select from the Above Options")

# Entry point of the program
if __name__ == '__main__':
    start()
                  
