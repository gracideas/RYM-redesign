from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':  # lets you just f5 to see changes w/o restart
    app.run(debug=True)
