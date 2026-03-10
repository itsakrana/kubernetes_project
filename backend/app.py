from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ✅ Change 1: Set initial tasks as completed = True
tasks = [
    {"id": 1, "title": "Learn Docker", "completed": True, "created_at": "2026-03-10T10:00:00"},
    {"id": 2, "title": "Build Task Manager", "completed": True, "created_at": "2026-03-10T10:05:00"}
]

def get_task(task_id):
    return next((task for task in tasks if task["id"] == task_id), None)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"status": "success", "tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"status": "error", "message": "Title is required"}), 400
    
    # ✅ Change 2: New tasks are completed by default
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": True,  # change here
        "created_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    return jsonify({"status": "success", "task": new_task}), 201

@app.route('/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    task = get_task(task_id)
    if not task:
        return jsonify({"status": "error", "message": "Task not found"}), 404
    task["completed"] = not task["completed"]
    return jsonify({"status": "success", "task": task})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = get_task(task_id)
    if not task:
        return jsonify({"status": "error", "message": "Task not found"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"status": "success", "message": "Task deleted"})

@app.route('/')
def home():
    return jsonify({"status": "success", "message": "Backend is running. Visit /tasks to see tasks."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
