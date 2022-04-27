from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<p>Hello, World!</p>'


@app.route("/harmith")
def harmith():
    return '<h1>Hello Harmith</h1>'


# setting 'debug=True' will make the app auto-reload whenever we make some changes in the backend
# on final run, remove this as default debug=False
app.run(debug=True)
