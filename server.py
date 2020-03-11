from flask import Flask

app = Flask(__name__)

players = 0

@app.route("/")
def index():
    return "Chess Server running."

