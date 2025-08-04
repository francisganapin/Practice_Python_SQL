from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    user_logged_in = True
    if user_logged_in:
        message = 'Welcome Back!'
    else:
        message = "Hello,GUEST"
    
    return render_template('index.html',message=message)