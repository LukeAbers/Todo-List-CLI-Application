import sys
import os

# File to save/load tasks
FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        for task in tasks:
            f.write(f"{task}\n")

def list_tasks(tasks):
    if not tasks:
        print("No tasks added yet!")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTodo List CLI")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
