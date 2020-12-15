from models import Person, Task, Project
import datetime

def seed(db):
    persons = [
        Person(id=1, name="Joy Ann"),
        Person(id=2, name="Michael John"),
        Person(id=3, name="Laine Elizabeth"),
    ]

    projects = [
        Project(id=1, name="Online Store"),
        Project(id=2, name="Christmas Presents"),
    ]

    tasks = [
        Task(id=1, name="Inventory", description="Upload inventory to database", due_date=datetime.date(2020, 1, 1), completed=False, person_id=1, project_id=1),
        Task(id=2, name="Web design", description="Hire web designer", due_date=datetime.date(2020, 1, 1), completed=False, person_id=1, project_id=1),
        Task(id=3, name="Front end", description="Build front end", due_date=datetime.date(2020, 1, 1), completed=False, person_id=3, project_id=1),
        Task(id=4, name="Back end", description="Build back end", due_date=datetime.date(2020, 1, 1), completed=False, person_id=3, project_id=1),
        Task(id=5, name="Buy Joy laptop", description="Macbook Pro 16 inch", due_date=datetime.date(2020, 1, 1), completed=False, person_id=2, project_id=2),
        Task(id=6, name="Buy Laine coal", description="Home Depot", due_date=datetime.date(2020, 1, 1), completed=False, person_id=2, project_id=2),
    ]


    db.session.add_all(persons)
    db.session.add_all(tasks)
    db.session.add_all(projects)
    db.session.commit()