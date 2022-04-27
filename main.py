from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/about")
def about():
    person = 'Harmith'
    return render_template('about.html', name=person)


app.run(debug=True)
