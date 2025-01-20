from datetime import datetime
import json
import argparse

data = []

def write(data):
    with open("./DataBase/data.json", "w") as file:
        json.dump(data, file)
        
def read():
    with open("./DataBase/data.json", "r") as file:
        content = file.read()
        return json.loads(content) if content else []

data = read()

def add(description):
    global data
    next_id = max([task['id'] for task in data], default=0) + 1
    data.append({
        'id':next_id,
        'description':description,
        'status':'todo',
        'createdAt':str(datetime.now()),
        'updatedAt':str(datetime.now())
    })
    write(data)
    
def delete(id):
        global data
        new_data = [task for task in data if task['id'] != id]
        write(new_data)

def update(id,description):
    global data
    for row in data:
        if row['id'] == id:
            row['description'] = description
            row['updatedAt'] = str(datetime.now())
    write(data)

def list(status=None):
    print("Id Descipcion")
    global data
    for row in data:
        if status is None or row['status'] == status:
            print(f"{row['id']}  {row['description']}")

def mark_in_progress(id):
        global data
        for row in data:
            if row['id'] == id:
                row['status'] = 'in-progress'
        write(data)

def mark_done(id):
        global data
        for row in data:
            if row['id'] == id:
                row['status'] = 'done'
        write(data)

def main():
    parser = argparse.ArgumentParser(description="Task CLI")
    subparser = parser.add_subparsers(dest='command')
    
    parser_add = subparser.add_parser('add')
    parser_add.add_argument('description')
    
    parser_update = subparser.add_parser('update')
    parser_update.add_argument('id', type=int)
    parser_update.add_argument('description')
    
    parser_delete = subparser.add_parser('delete')
    parser_delete.add_argument('id', type=int)
    
    parser_in_progress = subparser.add_parser('mark-done')
    parser_in_progress.add_argument('id', type=int)
    
    parser_list = subparser.add_parser('list',)
    parser_list.add_argument('status', choices=['todo', 'in-progress', 'done'], nargs='?')
    
    while True:
        print("\nAvailable commands:")
        print("add        - Add a task")
        print("update     - Update a task")
        print("delete     - Delete a task")
        print("mark-done  - Mark a task as completed")
        print("mark-in-progress  - Mark a task as in progress")
        print("list       - List tasks")
        print("exit       - To quit")
        print("\nEnter a command (or type 'exit' to quit):")
        user_input = input().strip().split()
        
        if user_input[0] == 'exit':
            break
        
        try:
            args = parser.parse_args(user_input)
            if args.command == 'add':
                add(args.description)
            elif args.command == 'update':
                update(args.id, args.description)
            elif args.command == 'delete':
                delete(args.id)
            elif args.command == 'mark-done':
                mark_done(args.id)
            elif args.command == 'list':
                list(args.status)
        except SystemExit as e:
            continue

main()