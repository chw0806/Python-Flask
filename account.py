from flask import blueprints, render_template
ac =blueprints.Blueprint('ac', __name__)

@ac.route('/login', method=['GET','POST'])

def login():
    return render_template('login.html')