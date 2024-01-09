from flask import Flask

#This is the principal module
app = Flask(__name__)

@app.route('/') # if / is the main page 5000, however if I put main, it will show the the same url but with 5000/main
def hello():
    return 'Hello World Flask :D, ARE YOU SEEING THIS?'

if __name__ == '__main__':
    app.run(debug=True, port=5000)