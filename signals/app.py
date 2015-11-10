from flask import Flask

app = Flask('signals')


@app.route('/')
def hello():
    return 'Hello World!'
