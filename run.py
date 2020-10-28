import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []



def add_messages(username, message):
    """Add messages to messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}): {}: {}".format(now, username, message))


def get_all_messages():
    """Format messages list"""
    return "<br>".join(messages)


@app.route("/", methods=["get", "POST"])
def index():
    """Main page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect("/" + session["username"])

    return render_template("index.html")


@app.route("/<username>")
def name(username):
    """Display chat message"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect to chat message"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
            debug=True)
