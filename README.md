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


### Flask-SQLAlchemy


### Querying


<hr>
</details><br>


### 🖥 Review files
1. Blah blah blah
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
1. Blah blah blah
<br>





# Flask Variable Rules

<details><summary>💡 What is a variable rule in Flask?</summary>
<hr>

### Variable Rules



<hr>
</details><br>


### 🖥 Write a simple route for `GET /tasks/{id}`
1. Blah blah blah
<br>





# Flask Request Object

<details><summary>💡 What is the request object in Flask?</summary>
<hr>

### `request` Object


### `request.method`


<hr>
</details><br>


### 🖥 Let's extend that route to handle `DELETE /tasks/{id}`
1. Blah blah blah
<br>





### 🖥 Let's write a route that handles completing a task: `PUT /tasks/{id}/complete`
1. Blah blah blah
<br>






# Flask Query Parameters

<details><summary>💡 What is query parameter in Flask?</summary>
<hr>

### `request` Object


### `request.args`


<hr>
</details><br>


### 🖥 Let's write a route to handle querying by a person's name `GET /tasks/query?person={person}`
1. Blah blah blah
<br>





# That's it! You did it! Great job! 👏
Feel free to practice some more by writing project routes!
