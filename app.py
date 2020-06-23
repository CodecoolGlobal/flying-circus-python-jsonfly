import data

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Return this to the user who visited this page. The browser will render it.
    return 'Hello World!'

if __name__ == '__main__':
    app.run()