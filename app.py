#app.py

from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello():
    return 'Hello World, this my first app with flask.'

if __name__ == '__main__': 
    app.run(debug=True)