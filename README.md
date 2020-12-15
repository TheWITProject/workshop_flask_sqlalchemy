# the \<wit\> project workshop: "flask & sql-alchemy"


_Anytime you see a 🖥, follow the instructions below. Anytime you see a 💡, click the toggles to find more information._
<br><br>


### 🖥 Install this project locally
1. Clone this repo: `git clone <this repo's remote url>`
2. Change directories: `cd workshop_flask_sqlalchemy`
3. Create a virtual environment for this project and activate it:
```
mkdir env
python3 -m venv env
source env/bin/activate
```
4. Install the requirements: `pip install -r requirements.txt`
5. If you haven't done so already, create a database named `todo`
6. Run `python app/db.py` to create and seed your database tables
7. Run the application as needed: `python app/app.py`
<br>





# Flask

<details><summary>💡 What is a Flask?</summary>
<hr>

### Flask
Flask is a lightweight but extensible framework for building web applications using Python. By extending [Werkzeug](https://werkzeug.palletsprojects.com/) and [Jinja](http://jinja.pocoo.org/docs), Flask provides tools to handle various functionalities, like URL routing and templating. You can find documentation for Flask [here](https://flask.palletsprojects.com/en/1.1.x/).

### Flask-SQLAlchemy
Flask-SQLAlchemy is an extension for Flask that adds support for SQL-Alchemy to your application by providing useful defaults and helpers that make it easier to accomplish common tasks. Because SQL-Alchemy is already intgreated into the Flask package, the setup is slightly different from what you may be used to from using SQL-Alchemy alone. You can find documentation for setup [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) and documentation for Flask-SQLAlchemy [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/). 

<hr>
</details><br>


### 🖥 Review files
1. `app/app.py`<br>
This is where the basic boilerplate for your app is set up. Confirm that the URI on line 6 correctly points to your database. It is set as a configuration variable to `app` before you database app is instantiated and set to the `db` variable on line 8. On line 12, you can see that we import all of our routes (`import *`) from `app/api.py`. On line 13, we invoke the `run` method on `app` to start our development server. If you run this file (`python app/app.py)`, you'll see some feedback in your terminal saying you are now running a local server on port 5000.
2. `app/db.py`<br>
This file is responsible for creating and seeding your database tables. You'll see we import the `db` object from `app/app.py` and the `seed` function from `app/seed.py` on lines 1 and 2. If you run this file (`python app/db.py`), you'll see some feedback in your terminal and then be able to see changes to your database using `psql` or your chosen GUI.
3. `app/models.py`<br>
Your models are defined by `app/models.py`. You'll notice that all of the SQL helpers are invoked off of the `db` object create in `app/app.py`.
<br>





# Routing

<details><summary>💡 How do we write a route in Flask?</summary>
<hr>

### Routing Syntax


<hr>
</details><br>


# Querying

<details><summary>💡 What is a query?</summary>
<hr>

### `query` method
- `query.all()`
- `query.get(<id>)`
- `query.filter(<expression>)`

<hr>
</details><br>


### 🖥 Write a simple route for `GET /tasks/`
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py
@app.route('/tasks', methods=['GET'])
def all_tasks():
    data = Task.query.all()
    all_tasks = [item.serialize() for item in data]
    return jsonify(all_tasks)

```

<hr>
</details>
<br>





# Flask Variable Rules

<details><summary>💡 What is a variable rule in Flask?</summary>
<hr>

### Variable Rules



<hr>
</details><br>


### 🖥 Write a simple route for `GET /tasks/{id}`
In `app/api.py`, write a simple route to get a task by primary key from your database. You can use the `Task.query.get(<id>)` method.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_or_delete_one_task(task_id):
    data = Task.query.get(task_id)
    one_task = data.serialize()
    return jsonify(one_task)

```

<hr>
</details>
<br>





# Flask Request Object

<details><summary>💡 What is the request object in Flask?</summary>
<hr>

### `request` Object


### `request.method`


<hr>
</details><br>


### 🖥 Let's extend that route to handle `DELETE /tasks/{id}`
In `app/api.py`, extend the `/tasks/{id} route you wrote to get a task by primary key so that the route can be used to delete a task by primary key. You can use the `db.session.delete(<id>)` method.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py
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

```

<hr>
</details>
<br>





### 🖥 Let's write a route that handles completing a task: `PUT /tasks/{id}/complete`
In `app/api.py`, write a simple route to set a task to completed.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py
@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    data = Task.query.get(task_id)
    data.completed = True
    db.session.commit()
    return "Completed"

```

<hr>
</details>
<br>






# Flask Query Parameters

<details><summary>💡 What is query parameter in Flask?</summary>
<hr>

### `request` Object


### `request.args`


<hr>
</details><br>


### 🖥 Let's write a route to handle querying by a person's name `GET /tasks/query?person={person}`
In `app/api.py`, write a simple route to get all tasks by a query search of someone's name. You can use the `request.args` object to access the query parameter value. Then, you can use the `Person.query.filter(<expression>)` method to find that person's tasks.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py
@app.route('/tasks/field')
def get_all_tasks_by_person():
    person = request.args.get("person")
    person_id = Person.query.filter(Person.name == person).first().id
    data = Task.query.filter(Task.person_id == person_id).all()
    all_tasks_of_person = [item.serialize() for item in data]
    return jsonify(all_tasks_of_person)

```

<hr>
</details>
<br>





# That's it! You did it! Great job! 👏
Feel free to practice some more by writing project routes!
