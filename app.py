from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome everyone!'

@app.route('/greet')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def hello_user(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
