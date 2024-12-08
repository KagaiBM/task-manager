# delete_task.py
tasks = []
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task deleted: {task}")
    else:
        print("Task not found.")
