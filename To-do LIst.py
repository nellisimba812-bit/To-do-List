import json

def load_todos():
    try:
        with open('todos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

todos = load_todos()  #Список всех задач

def save_todos():
    with open('todos.json', 'w') as f:
        json.dump(todos, f)

def add_task(): #Добавляет задачу
    text = input("Input a task: ")
    task = {"text": text, "done": False}
    todos.append(task)
    save_todos()
    print('A task has been added')

def edit_task(): #Редактирует задачу
    try:
        show_todos()
        ind = int(input("Which task would you like to edit?: "))
        todos[ind - 1]["text"] = input("Input a edit task: ")
        save_todos()
        print('A task has been edited')
    except (ValueError, IndexError):
        print('Invalid command')

def show_todos():   #Показывает все задачи
    for i, task in enumerate(todos):
        print(f'{i+1}. {task["text"]}; Is done? {task["done"]}')

def mark_done(): #Отмечает выполненным
    try:
        show_todos()
        ind = int(input("Select an option: "))
        todos[ind - 1]["done"] = True
        save_todos()
        print('A task has been marked done')
    except (ValueError, IndexError):
        print('Invalid command')


def delete_task():  #Удаляет задачу
    try:
        show_todos()
        ind = int(input("Select an option: "))
        todos.pop(ind - 1)
        save_todos()
        print('A task has been deleted')
    except (ValueError, IndexError):
        print('Invalid command')

while True:
    print('|||||||')
    print('1. Add a task')
    print('2. Edit task')
    print('3. Mark done')
    print('4. Delete task')
    print('5. Show todos')
    print('6. Exit')
    command = input('What would you like to do?: ')

    if command == '6':
        print('Goodbye!')
        break

    elif command == '1':
        add_task()

    elif command == '2':
        edit_task()

    elif command == '3':
        mark_done()

    elif command == '4':
        delete_task()

    elif command == '5':
        show_todos()

    else:
        print('Invalid command')