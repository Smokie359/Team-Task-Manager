# view_task.py

tasks = [
    {"id": 1, "title": "Do homework", "status": "Pending"},
    {"id": 2, "title": "Buy groceries", "status": "Completed"},
    {"id": 3, "title": "Clean room", "status": "Pending"}
]

def view_all_tasks():
    """
    Display all tasks in a formatted way.
    """
    print("------ All Tasks ------")
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")
    print("-----------------------")


# Ye part sirf testing ke liye hai
if __name__ == "__main__":
    view_all_tasks()
