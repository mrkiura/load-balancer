import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def sample():
    return f"This is a {os.environ['APP']} application."


@app.route("/healthcheck")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
