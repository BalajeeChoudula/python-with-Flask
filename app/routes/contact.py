from flask import Flask,Blueprint, request,render_template

contact = Blueprint('contact',__name__)

@contact.route('/contact')
def index():
    return render_template('contact.html')