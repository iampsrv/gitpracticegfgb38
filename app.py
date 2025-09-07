from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome everyone!'

@app.route('/abc')
def hello_world():
    return 'Hello, Everyone!'



import os

# New route to display the value of an environment variable
@app.route('/showenv')
def show_env():
    env_var = os.getenv('MY_SECRET_VAR', 'Variable not set')
    return f'MY_SECRET_VAR: {env_var}'

@app.route('/greet')
def hello_world():
    return 'Hello, World!'

@app.route('/<username>')
def hello_user(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
