from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/futureself')
def hello_future():
    return 'Hello, future self!'

if __name__ == '__main__':
    app.run()
