from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return {'msg':"welcome with sync 2024!"}

@app.route('/hello')
def hi():
    return 'hello world 2024!'

