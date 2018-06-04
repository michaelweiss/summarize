from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Bad request</h1>", 400

@app.route("/user/<name>")
def user(name):
    return "hello, {}!".format(name)