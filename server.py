from flask import Flask

app = Flask(__name__)

players = 0

@app.route("/")
def index():
    return "Chess Server running."

if __name__ == "__main__":
    app.run(host="0.0.0.0")