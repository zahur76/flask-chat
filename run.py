import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use/USERNAME/MESSAGE"


@app.route("/<username>")
def name(username):
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return ("{0}: {1}").format(username, message)


app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
            debug=True)
