from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp())

# data model for Users
class Users(Base):
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(7))

# data model for Courses
class Courses(Base):
    number = db.Column(db.Integer)
    section = db.Column(db.Integer)
    term = db.Column(db.String(7))

# data model for Attendance
class Attendance(Base):
    # an 'Attendance' record is a unique id bound to a specific user instance and course instance
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))


    