import os
import json
from flask import render_template, request, redirect, url_for
from app import app

DATA_FILE = "app/data/todos.json"


def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todo_list):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(todo_list, f)


todos = load_todos()


@app.route('/')
def index():
    global todos
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    global todos
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
        save_todos(todos)
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    global todos
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
        save_todos(todos)
    return redirect(url_for('index'))
