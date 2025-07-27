from flask import Flask,Blueprint,render_template

home = Blueprint('home', __name__)
@home.route('/')
@home.route('/home')
def index():
    return render_template('home.html')