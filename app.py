from flask import *


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cname = request.form.get("cname")
        password = request.form.get("password")
        ename = request.form.get("ename")
        print(cname, password, ename)

    return render_template("test.html")

# @app.route("")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)