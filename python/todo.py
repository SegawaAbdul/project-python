# # add a task
# # remove a task
# # list all tasks
# # mark task as complete
# #save / load tasksfrom a file
# # task filtering
import functools
import json
import logging as trac
from functools import wraps

trac.basicConfig(filename='trace.log', level=trac.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def ace(func):
    @functools.wraps(func)
    def rea(*args,**kwargs):
        trac.info(f"{func.__name__} called with arguments:{args},{kwargs}")
        trac.debug(f"{func.__name__}called with args:{args}, kwargs:{kwargs}")
        result=func(*args,**kwargs)
        trac.info(f"{func.__name__} returned :{result}")
        return result
    return rea
tasks = []

@ace
def load_tasks():
    global tasks
    try:
        with open('.file.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return 'empty'

@ace
def write_tasks():
    with open('.file.json', 'w') as file:
        json.dump(tasks, file, indent=2)

@ace
def append_task():
    title = input("Enter the task name: ")
    desc = input("Enter the task description: ")
    tasks.append({"title": title, "description": desc})
    write_tasks()
    print(f'{title} added successfully')

@ace
def pop_task():
    if not tasks:
        print("No tasks available.")
        return
    task_no = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        del tasks[task_no]
        write_tasks()
        print(f"Task {task_no + 1} has been successfully deleted")
    else:
        print("Invalid task number.")

@ace
def dis_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\n\t\tYour Tasks:")
    print('_' * 25)
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task.get("completed", False) else "[ ]"
        print(f"|    status :{status} Task number {i}. Task {task['title']} :=> {task['description']}")
    print('_'*50)
@ace
def mark_task():
    if not tasks:
        print("No tasks available.")
        return
    task_no = int(input("Enter task number to mark as complete: "))
    if 0 <= task_no < len(tasks):
        tasks[task_no]["completed"] = True
        write_tasks()
        print(f"Task {task_no } has been marked as completed successfully")
    else:
        print("Invalid task number.")

@ace
def main():
    global tasks
    tasks = load_tasks()

    while True:
        sep,end='='*50,'='*17
        print(f"""\n\n{sep}\n{end} Todo List Menu {end}
       1. Lists
       2. Add Task
       3. Delete Task
       4. Mark Task as Complete
       5. Exit\n""")

        choice = input("Enter your choice (1-5): ____")
        trac.info(f"selected: {choice}")
        try:
            if choice == '1':
                dis_tasks()
            elif choice == '2':
                append_task()
            elif choice == '3':
                pop_task()
            elif choice == '4':
                mark_task()
            elif choice == '5':
                print(f'\n\n{end} end {end}')
                break

            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")
            trac.error(f"Value error:\n{ValueError}")
if __name__ == "__main__":
    main()

