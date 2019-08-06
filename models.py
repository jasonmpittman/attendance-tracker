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
    code = db.Column(db.String(10))
    section = db.Column(db.Integer)
    term = db.Column(db.String(7))

# data model for Attendance
class Attendance(Base):
    # an 'Attendance' record is a unique id bound to a specific user instance
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    key = db.Column(db.String(100))

    def __init__(self, attend_time, mod_time, user_id, course_id, key):
        self.date_created = attend_time
        self.date_modified = mod_time
        self.user_id = user_id
        self.course_id = course_id
        self.key = key


    