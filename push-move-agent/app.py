# This should be replaced with your starter code!

from flask import Flask

app = Flask(__name__)
@app.route('/')
def test():
    return "test"

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
