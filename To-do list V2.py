import json
import argparse

parser = argparse.ArgumentParser(description='To-do list')

subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser("add", help='Добавить задачу')
add_parser.add_argument('text', type=str)

edit_parser = subparsers.add_parser("edit", help='Редактировать задачу по номеру')
edit_parser.add_argument('index', type=int)
edit_parser.add_argument('text', type=str)

list_parser = subparsers.add_parser("list", help='Показать все задачи')

done_parser = subparsers.add_parser("done", help='Отметить выполненным по номеру')
done_parser.add_argument('index', type=int)

delete_parser = subparsers.add_parser("delete", help='Удалить задачу по номеру')
delete_parser.add_argument('index', type=int)

args = parser.parse_args()

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

def add_task(text): #Добавляет задачу
    task = {"text": text, "done": False}
    todos.append(task)
    save_todos()
    print('A task has been added')

def edit_task(index, text): #Редактирует задачу
    try:
        todos[index - 1]["text"] = text
        save_todos()
        print('A task has been edited')
    except IndexError:
        print('The index does not exist')

def show_todos():   #Показывает все задачи
    for i, task in enumerate(todos):
        print(f'{i+1}. {task["text"]}; Is done? {task["done"]}')

def mark_done(index): #Отмечает выполненным
    try:
        todos[index - 1]["done"] = True
        save_todos()
        print('A task has been marked done')
    except IndexError:
        print('The index does not exist')

def delete_task(index):  #Удаляет задачу
    try:
        todos.pop(index-1)
        save_todos()
        print('A task has been deleted')
    except IndexError:
        print('The index does not exist')

#Запуск через команды в терминале
if args.command == "add":
    add_task(text=args.text)

elif args.command == "edit":
    edit_task(index=args.index, text=args.text)

elif args.command == "list":
    show_todos()

elif args.command == "done":
    mark_done(index=args.index)

elif args.command == "delete":
    delete_task(index=args.index)

#Запуск через меню
elif args.command is None:

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
            try:
                add_task(text=input("Input a task: "))
            except IndexError:
                print('Please enter a valid number')


        elif command == '2':
            try:
                show_todos()
                edit_task(index=int(input("Select an option: ")), text=input("Input a edit task: "))
            except ValueError:
                print('Please enter a valid number')

        elif command == '3':
            try:
                show_todos()
                mark_done(index=int(input("Select an option: ")))
            except ValueError:
                print('Please enter a valid number')

        elif command == '4':
            try:
                show_todos()
                delete_task(index=int(input("Select an option: ")))
            except ValueError:
                print('Please enter a valid number')

        elif command == '5':
            show_todos()

        else:
            print('Invalid command')


