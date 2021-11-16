# imports ....
from flask import Flask, render_template, request, jsonify, send_from_directory
import webbrowser
from markupsafe import escape

# variables....
app = Flask(__name__, static_url_path='')

# functions...


@app.route("/")
def main_page():
    return render_template("ContentHome.html")


@app.route("/home")
def home():
    return render_template("ContentHome.html")


@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/references")
def references():
    return render_template("References.html")


@app.route("/<name>")
def slash_name(name):
    return f"hello, {escape(name)}!"


@app.route('/action_form', methods=['POST'])
def action_form():
    # -> prints the output to the terminal along with the flask data
    print(request.form['txtinput'] + " attachment")
    response = request.form['txtinput']

    # -> sends the content back to the webpage
    return f"hello, {escape(response)}!"

# functions


if __name__ == "__main__":
    app.run()
