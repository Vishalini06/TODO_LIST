import json

TODO_FILE = "todo_list.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):     
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file,indent=2)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📌 No tasks found!")
        return

    print("\n📌 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {status} {task['task']}")

# Mark a task as completed
def complete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"✔️ Task {task_number} marked as completed!")
    else:
        print("⚠️ Invalid task number!")

# Delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed_task['task']}")
    else:
        print("⚠️ Invalid task number!")

# Main Menu
def main():
    while True:
        print("\n📌 TO-DO LIST MENU:")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task as Completed")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_num = int(input("Enter task number to complete: "))
            complete_task(task_num)
        elif choice == "4":
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
