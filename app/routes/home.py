from flask import Flask,Blueprint, render_template

home = Blueprint('home', __name__)
@home.route('/')
@home.route('/home')
def index():
    print("Home route accessed")
    return render_template('home.html')

@home.before_request
def before_request():
    print("A request is about to be processed")
    # You can add more logic here if needed

@home.after_request
def after_request(response):
    print("A request has been processed")
    return response

@home.teardown_request
def teardown_request(exception):
    if exception:
        print(f"An error occurred: {exception}")
    else:
        print("Request completed successfully")
    # You can add more cleanup logic here if needed