from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {escape(name.capitalize())}'

if __name__ == '__main__':
    app.run(debug=True)
