from flask import request, jsonify
from app import app, db
from models import Person, Task, Project


# ------------------------------------------------
# TASK ROUTES
# ------------------------------------------------

# GET /tasks
@app.route('/tasks', methods=['GET'])
def all_tasks():
    return


# GET /tasks/{id},
# DELETE /tasks/{id}
@app.route('/tasks/<int:task_id>', methods=['GET', 'DELETE'])
def get_or_delete_one_task(task_id):
    return


# PUT /tasks/{id}/complete
@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    return


# GET /tasks/query?person={person}
@app.route('/tasks/field')
def get_all_tasks_by_person():
    return


# ------------------------------------------------
# PROJECT ROUTES
# ------------------------------------------------

# GET /projects
@app.route() # <-- fill in route and methods here
def all_projects():
    return


# GET /projects/{id}
@app.route()  # <-- fill in route and methods here
def get_one_project(): # <-- give the argument a name
    return

