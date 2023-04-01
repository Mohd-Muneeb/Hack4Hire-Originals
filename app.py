from flask import *


app = Flask(__name__)


@app.route("/")
def home():
    return "HEllo world"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)