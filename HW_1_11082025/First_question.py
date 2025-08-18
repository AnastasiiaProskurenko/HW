from flask import Flask
app = Flask(__name__)
@app.route('/')  # Очень важно порставлять "/" это как главная страница, точка входа приложения
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True) #При отладке желательно проставлять True, но для полноценно работающего веб-приложение, важно проставлять False