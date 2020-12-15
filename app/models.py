from app import db


class Person(db.Model):
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    tasks = db.relationship("Task", back_populates="person")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    due_date = db.Column(db.Date)
    completed = db.Column(db.Boolean)
    
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    person = db.relationship("Person", back_populates="tasks")
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship("Project", back_populates="tasks")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date,
            "person_id": self.person_id,
            "project_id": self.project_id
        }
  
  
class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    tasks = db.relationship("Task", back_populates="project")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }