from flask_admin.contrib.sqla import ModelView
from flask import session, redirect, url_for, request
from models import Users

class AdminView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'
    
    def is_accessible(self):
        #name = session['user']
        #user = Users.query.filter_by(username=name).first()
        #return user.role == 'faculty'
        return session.get('user') == 'Administrator'
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('home', next=request.url))