# imports ....
from flask import Flask, render_template, request, jsonify
import webbrowser

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("ContentHome.html")

@app.route('/', methods=['POST'])
def handle_form():
    print("here")
    return (request.form['txtinput'])

# functions

if __name__ == "__main__": 
    app.run()

