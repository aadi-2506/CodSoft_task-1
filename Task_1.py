import json

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, t in enumerate(self.tasks, 1):
                status = "Done" if t['completed'] else "Pending"
                print(f"{idx}. {t['task']} [{status}]")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("---------x---------")
        choice = input("Choose an option: ")

        if choice == '1':
            todo.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == '3':
            todo.view_tasks()
            task_num = int(input("Enter task number to mark completed: "))
            todo.mark_completed(task_num)
        elif choice == '4':
            todo.view_tasks()
            task_num = int(input("Enter task number to delete: "))
            todo.delete_task(task_num)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()