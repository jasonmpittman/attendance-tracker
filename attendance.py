from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Users

attendance = Flask(__name__)

# load our configuration
attendance.config.from_object('config')

# init our db
db.init_app(attendance)
db.create_all(app=attendance)

@attendance.route('/')
def home():
    return render_template('index.html')

@attendance.route('/signup')
def signup():
    return render_template('signup.html')

@attendance.route('/login')
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
    
    return redirect(request.args.get('next') or url_for('home')) 

if __name__ == '__main__':
    attendance.run()