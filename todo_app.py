import os
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Define the file to store tasks
TODO_FILE = "todo_list.txt"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            tasks = [task.strip() for task in f.readlines()]
    else:
        tasks = []
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Function to display tasks
def show_tasks(tasks):
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.CYAN + "        Your To-Do List        ")
    print(Fore.CYAN + "="*40)
    
    if not tasks:
        print(Fore.YELLOW + "\nYour to-do list is empty!\n")
    else:
        for i, task in enumerate(tasks, start=1):
            print(Fore.GREEN + f"{i}. {task}")
    print(Fore.CYAN + "="*40 + "\n")

# Function to add a task
def add_task(tasks):
    task = input(Fore.CYAN + "Enter the task: " + Fore.WHITE)
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + f"Task '{task}' added successfully!\n")

# Function to update a task
def update_task(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input(Fore.CYAN + "Enter the task number to update: ")) - 1
        if 0 <= task_no < len(tasks):
            updated_task = input(Fore.CYAN + "Enter the new task: " + Fore.WHITE)
            tasks[task_no] = updated_task
            save_tasks(tasks)
            print(Fore.GREEN + f"Task {task_no + 1} updated successfully!\n")
        else:
            print(Fore.RED + "Invalid task number.\n")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number.\n")

# Function to delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input(Fore.CYAN + "Enter the task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            deleted_task = tasks.pop(task_no)
            save_tasks(tasks)
            print(Fore.GREEN + f"Task '{deleted_task}' deleted successfully!\n")
        else:
            print(Fore.RED + "Invalid task number.\n")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number.\n")

# Function to show the menu
def show_menu():
    print(Fore.MAGENTA + "===============================")
    print(Fore.MAGENTA + "         To-Do List Menu        ")
    print(Fore.MAGENTA + "===============================")
    print(Fore.YELLOW + "1. View tasks")
    print(Fore.YELLOW + "2. Add a task")
    print(Fore.YELLOW + "3. Update a task")
    print(Fore.YELLOW + "4. Delete a task")
    print(Fore.YELLOW + "5. Exit")
    print(Fore.MAGENTA + "===============================\n")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        try:
            choice = int(input(Fore.CYAN + "Choose an option (1-5): " + Fore.WHITE))
            if choice == 1:
                show_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print(Fore.CYAN + "Goodbye! Have a productive day!")
                break
            else:
                print(Fore.RED + "Invalid option, please choose between 1 and 5.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()
