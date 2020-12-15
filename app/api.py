from flask import request, jsonify
from app import app, db
from models import Person, Task, Project


# ------------------------------------------------
# TASK ROUTES
# ------------------------------------------------

# GET /tasks
@app.route('/tasks', methods=['GET'])
def all_tasks():
    data = Task.query.all()
    all_tasks = [item.serialize() for item in data]
    return jsonify(all_tasks)


# GET /tasks/{id},
# DELETE /tasks/{id}
@app.route('/tasks/<int:task_id>', methods=['GET', 'DELETE'])
def get_or_delete_one_task(task_id):
    data = Task.query.get(task_id)

    if request.method == 'DELETE':
        db.session.delete(data)
        db.session.commit()
        return "Deleted"
    else:
        one_task = data.serialize()
        return jsonify(one_task)


# PUT /tasks/{id}/complete
@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    data = Task.query.get(task_id)
    data.completed = True
    db.session.commit()
    return "Completed"


# GET /tasks/query?person={person}
@app.route('/tasks/field')
def get_all_tasks_by_person():
    person = request.args.get("person")
    person_id = Person.query.filter(Person.name == person).first().id
    data = Task.query.filter(Task.person_id == person_id).all()
    all_tasks_of_person = [item.serialize() for item in data]
    return jsonify(all_tasks_of_person)


# ------------------------------------------------
# PROJECT ROUTES
# ------------------------------------------------

# GET /projects
@app.route('/projects', methods=['GET'])
def all_projects():
    data = Project.query.all()
    all_projects = [item.serialize() for item in data]
    return jsonify(all_projects)


# GET /projects/{id}
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_one_project(project_id):
    data = Project.query.get(project_id)
    one_project = data.serialize()
    return jsonify(one_project)

