from flask import Flask, Blueprint, render_template
pagenotfound = Blueprint('pagenotfound', __name__)
@pagenotfound.route('/pagenotfound')
def index():
    print("Page Not Found route accessed")
    return render_template('pagenotfound.html')