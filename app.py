from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "SDC12345"

# Database Employees
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Employee( db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    company = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Integer, nullable=False)

class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable = False)
    mobile = db.Column(db.Integer, nullable = False)
    email = db.Column(db.Text, nullable= False)
    can_email= db.Column(db.Integer, nullable=False)
    can_mobile= db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

    

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

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method: pass


@app.route("/members")
def members():
    return "members"


@app.route("/customers")
def customers():
    return "customers"


@app.route("/register")
def register():
    return "register"


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)