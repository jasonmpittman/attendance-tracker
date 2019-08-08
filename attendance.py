from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_admin import Admin
from admin import AdminView
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Users, Attendance, Courses
from datetime import datetime

attendance = Flask(__name__)

# load our configuration
attendance.config.from_object('config')

# init our db
db.init_app(attendance)

# uncomment if the db needs to be created
#db.create_all(app=attendance)

# admin dashboard stuff
admin = Admin(attendance, name='Dashboard', index_view=AdminView(Attendance, db.session, url='/admin', endpoint='admin'))
admin.add_view(AdminView(Users, db.session))
admin.add_view(AdminView(Courses, db.session))

# route for default/home path
@attendance.route('/')
def home():
    return render_template('index.html')

# default route for faculty role
@attendance.route('/faculty')
def faculty():
  return render_template('faculty.html')

# route for faculty attendance search
@attendance.route('/searchattend', methods=['GET', 'POST'])
def searchattend():
    results = Attendance.query.all() # need to run the joins here?
 
    if not results:
        flash('No results found')
        return redirect(url_for('faculty'))
    else:
        return render_template('faculty.html', table=results)

# route for user sign up path
@attendance.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password = generate_password_hash(password)

        user = Users(username=username, password=password, role='student')

        db.session.add(user)
        db.session.commit()

        flash('Thanks for signing up! You can login now.')
        return redirect(url_for('home'))

    return render_template('signup.html')

# route for user login path
@attendance.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = Users.query.filter_by(username=username).first()

    if user:
        password_hash = user.password

        if check_password_hash(password_hash, password):
            session['user'] = username
            flash('Login successful')
    else:
        flash('Username or password is incorrect')
    
    if user.role == 'student':
        return redirect(request.args.get('next') or url_for('home')) 
    
    if user.role == 'faculty':
        return redirect(request.args.get('next') or url_for('faculty'))

# route for user logout path
@attendance.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')

        flash('Thanks for attending!')
    
    return redirect(url_for('home'))

# route for attendance path
@attendance.route('/attendance', methods=['GET'])
def attend():
    if 'user' in session:
        return render_template('attendance.html')
    else:
        flash('Please login to submit attendance')
    
    return redirect(url_for('home'))

# route for addattend path from attendance.js/html
@attendance.route('/addattend', methods=['GET', 'POST'])
def addattend():
    
    if request.method == 'POST':
        attend_time = datetime.now()
        mod_time = datetime.now()
        user = Users.query.filter_by(username=session['user']).first()
        course = Courses.query.filter_by(code=request.form['course']).first()
        section = Courses.query.filter_by(section=request.form['section']).first()
        key = request.form['key']
        print('user {} present in {}', user.id, course.id, course.section, key)
        
        #need to validate what the student submits based on what is registered in Courses. how to error handle (try-catch)            
        

        # build the attendance record and write to db
        attendee = Attendance(attend_time, mod_time, user.id, course.id, key)
        db.session.add(attendee)
        db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    attendance.run()