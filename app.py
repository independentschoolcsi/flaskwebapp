from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jason')
def hello_name():
    return 'Hello, Jason!'

if __name__ == '__main__':
    app.run()
