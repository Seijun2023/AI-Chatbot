from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World Flask :D, ARE YOU SEEING THIS?'

if __name__ == '__main__':
    app.run(debug=True, port=5000)