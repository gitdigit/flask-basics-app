# flask-basics-app
Repository to learn the basics of flask. The following commands only work for MacOS and Linux, please check the equivalent commands for Windows.

1. Go to your project repository to create the virtual environment 
```
python3 -m venv venv
```

2. Activate the virtual environment
```
source venv/bin/activate
```

3. Install Flask
```
pip install Flask  
```

4. Add a app.py file in the repository 
```
#app.py

from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello():
    return 'Hello World, this my first app with flask.'

if __name__ == '__main__': 
    app.run(debug=True)
```
4. Run the app
```
python3 app.py 
```
