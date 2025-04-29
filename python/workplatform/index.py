from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import datetime
from pathlib import Path

app = Flask(__name__)

# 确保数据目录存在
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "tasks.json"

# 初始化数据文件
if not DATA_FILE.exists():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False)

def load_tasks():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    task = request.json
    task['id'] = len(tasks) + 1
    task['created_at'] = datetime.datetime.now().isoformat()
    task['status'] = 'active'  # active, completed, deleted
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    task_data = request.json
    
    for task in tasks:
        if task['id'] == task_id:
            task.update(task_data)
            save_tasks(tasks)
            return jsonify(task)
    
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'completed'
            task['completed_at'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            return jsonify(task)
    
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'deleted'
            task['deleted_at'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            return jsonify(task)
    
    return jsonify({"error": "Task not found"}), 404

@app.route('/list')
def task_list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)
