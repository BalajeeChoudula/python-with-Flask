from flask import Flask, Blueprint, render_template
pagenotfound = Blueprint('pagenotfound', __name__)
@pagenotfound.route('/pagenotfound')
def index():
    return render_template('pagenotfound.html')