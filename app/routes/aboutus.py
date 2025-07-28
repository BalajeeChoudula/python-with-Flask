from flask import Flask, Blueprint, render_template
aboutus = Blueprint('aboutus', __name__)

@aboutus.route('/aboutus')
def index():
    print("About Us route accessed")
    return render_template('aboutus.html')