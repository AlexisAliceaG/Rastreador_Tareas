from datetime import datetime
import json

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
