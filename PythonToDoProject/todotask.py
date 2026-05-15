# This is python project for to do in python : 

tasks = []


def show_menu():
    print("\n===== TO DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")



def view_tasks():

    if len(tasks) == 0:
        print("\nNo tasks available.")

    else:
        print("\nYour Tasks:")

        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")


def add_task():

    task = input("\nEnter new task: ")

    tasks.append(task)

    print("Task added successfully!")



def remove_task():

    if len(tasks) == 0:
        print("\nNo tasks to remove.")
        return

    print("\nYour Tasks:")

    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

    try:
        task_number = int(input("\nEnter task number to remove: "))

        if 1 <= task_number <= len(tasks):

            delete_task = tasks.pop(task_number - 1)

            print(f"{delete_task} removed successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter numbers only.")


def main():

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                view_tasks()

            case "2":
                add_task()

            case "3":
                remove_task()

            case "4":
                print("\nExit 👋")
                break

            case _:
                print("\nInvalid choice.")



if __name__ == "__main__":
   main()