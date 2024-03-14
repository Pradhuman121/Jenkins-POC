from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! This is my CI/CD demo.'

if __name__ == '__main__':
    app.run(address=0.0.0.0 , debug=True) 
