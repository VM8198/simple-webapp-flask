import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello oia!"

@app.route('/how are you')
def hello():
    return 'I am good too, how about you?'

@app.route('/test')
def test():
    return 'Running well!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
