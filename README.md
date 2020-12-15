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
Flask-SQLAlchemy is an extension for Flask that adds support for SQL-Alchemy to your application by providing useful defaults and helpers that make it easier to accomplish common tasks. Because SQL-Alchemy is already integrated into the Flask package, the setup is slightly different from what you may be used to from using SQL-Alchemy alone. You can find documentation for setup [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) and documentation for Flask-SQLAlchemy [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/). 

<hr>
</details><br>


### 🖥 Review files
1. `app/app.py`<br>
This is where the basic boilerplate for your app is set up. As mentioned above, the boilerplate for SQlAlchemy is slightly different than what we wrote last week when we used SQLAlchemy on its own. The URI for your database is stored as a configuration attribute on the `app` object. On line 8, we run the `SQLAlchemy` function with `app` passed in to instantiate an database object that acts as both our enginer, sessionmaker, and declarative base. Confirm that the URI on line 6 correctly points to your database.<br>
On line 13, we invoke the `run` method on `app` to start our development server. If you run this file (`python app/app.py)`, you'll see some feedback in your terminal saying you are now running a local server on port 5000. You can now access this web app or its endpoints at http://localhost:5000/.
2. `app/models.py`<br>
Your models are defined by `app/models.py`. You'll notice that all of the table definitons extend `db.Model` as do any Flask-SQLAlchemy helpers, like `Column` or `String` or `Integer`. You might also notice that each model definition has a `serialize` mehtod in order to return data about our models in JSON. In the future, we might want to utilize a Python package that handles serialization for us.
3. `app/db.py`<br>
Our tables are created and seeded in this file. If you run this file (`python app/db.py`), you'll see some feedback in your terminal and then be able to see changes to your database using `psql` or your chosen GUI.
<br>





# Routing

<details><summary>💡 How do we write a route in Flask?</summary>
<hr>

### Routing Syntax
In Flask, routes are defined using the `route()` decorator, which binds a specific function to a URL rule. The `route()` decorator takes a URL rule as its first argument and any options as additional arguments. An option you will commonly provide is a list of HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, etc) that this particular route supports. The function that immediately follows the `route()` decorator is what it executed when an HTTP request hits the defined endpoint.

You can read more documentation about this [here](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route).

```py
@app.route('/', methods=['GET'])
def index():
    return 'Hello World'
```
<hr>
</details><br>


# Querying

<details><summary>💡 What is a query?</summary>
<hr>

### Queries
A query is a request to our database for data. Queries can request either general information or specific information depending on how they're written. In `Flask-SQLAlchemy`, each model receives a `query` attribute that lets us write queries off of that table.


### `query` attribute
The `query` attribute has many methods that you can use to shape the query you send to your database and you can read more about those [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records). In the meantime, let's focus on the following:
- `query.all()`<br>
This method will return all rows from your table in a list.
- `query.get(<id>)`<br>
This method allows you to query your table by primary key. The data is returned as a dictionary.
- `query.filter(<condition>)`<br>
This method allows you to query your table by some condition (e.g., `Task.name == 'Homework`). The data is returned as a list.


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
You can add variable sections to a URL by marking sections with `<variable_name>` (including the carrot brackets). Your function then receives the `<variable_name>` as a keyword argument. You can read more documentaiton on this [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules).

```py
@app.route('/<planet>', methods=['GET'])
def index(planet):
    return f'Hello {planet}'
```

### Converters
HTTP requests and responses are not written in a robust programming language like Python: there is no such thing as data types in these requests and responses; the data you send or recieve is formatted as strings. In Flask, you can use a converter to specify the data type of the argument likeso <converter:variable_name>. Flask then does the work of making sure your data is converted into the appropriate data type.

```py
@app.route('/<string:planet>', methods=['GET'])
def index(planet):
    return f'Hello {planet}'
```

A list of converters available includes `string`, `int`, `float`, `path`, and `uuid`.

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
In `app/api.py`, write a simple route to get all tasks by a query search of someone's name. You can use the `request.args` object to access the query parameter value. Then, you can use the `Person.query.filter(<condition>)` method to find that person's tasks.
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
