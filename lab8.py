from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Bonjour au lab 8 sur Flask </h1>"