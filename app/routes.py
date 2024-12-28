from flask import Blueprint, request, jsonify, render_template, request, redirect, url_for
from app.models import Task
from app.db import db

task_routes = Blueprint('tasks', __name__)

@task_routes.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Task Manager API!"})

# Get all tasks function where it fetches all the tasks from the database
@task_routes.route('/tasks', methods=['GET', 'POST'])
def get_tasks():
    if request.method == 'POST':
        task_id = request.json.get('task_id')  # Get task_id from JSON payload
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        task.completed = True
        db.session.commit()
        print(f"comit done for task {task_id}")
        return jsonify({'message': 'Task marked as completed', 'task_id': task_id, 'status': task.completed})

    # Fetch all tasks
    tasks = Task.query.order_by('id').all()
    return render_template('index.html', tasks=tasks)

# Create the task function where it takes the title and description and creates a new task
@task_routes.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        # Add a new task
        title = request.form["title"]
        desc = request.form["description"]
        # Missing due date and stauts here.
        new_task = Task(title=title, description=desc)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.get_tasks'))
    return render_template('create_task.html')

# Edit task function where it takes the task id and updates the task
@task_routes.route('/edit_task', methods=['GET', 'POST'])
def edit_task():
    task_id = request.args.get('task_id')
    tasks = Task.query.get(task_id)
    tasks_list = [tasks]
    if request.method == 'POST':
        tasks.title = request.form["title"]
        tasks.description = request.form["description"]
        tasks.completed = 'completed' in request.form 
        db.session.commit()
        return redirect(url_for('tasks.get_tasks'))
    return render_template('edit_task.html', tasks=tasks_list)

# Delete task function where it takes the task id and deletes the task
@task_routes.route('/delete_task', methods=['GET'])
def delete_task():
    task_id = request.args.get('task_id')
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

# Mark task as complete function where it takes the task id and marks the task as complete
from flask import jsonify

@task_routes.route('/mark_as_complete', methods=['POST'])
def mark_as_complete():
    pass
