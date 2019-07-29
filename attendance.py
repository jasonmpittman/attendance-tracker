from flask import Flask, flash, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Users

attendance = Flask(__name__)

# load our configuration
attendance.config.from_object('config')

# init our db
db.init_app(attendance)
db.create_all(app=attendance)

# route for default/home path
@attendance.route('/')
def home():
    return render_template('index.html')

# route for user sign up path
@attendance.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password = generate_password_hash(password)

        user = Users(username=username, password=password)

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
    
    return redirect(url_for('home')) 

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
@attendance.route('/here', methods=['GET', 'POST'])
def here():
    if request.method == 'POST':
        
            user = session['user']
            course = request.form['course']

            print(user + " is present in " + course)

    return redirect(url_for('home'))

if __name__ == '__main__':
    attendance.run()