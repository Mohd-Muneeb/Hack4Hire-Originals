from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__)
app.config["SECRET_KEY"] = "SDC12345"

# Database Employees
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db1 = SQLAlchemy(app)

class User( db1.Model):
    __tablename__ = "company1"
    id = db1.Column(db1.Integer, primary_key=True)
    ename = db1.Column(db1.Integer, nullable=False, unique=True)
    password = db1.Columm(db1.Text, nullable=False)
    company = db1.Column(db1.Text, nullable=False)
    is_admin = db1.Column(db1.Integer, nullable=False)

db1.create_all()

# Database Customer
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///customer.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db2 = SQLAlchemy(app)

class company1(db2.Model):
    __tablename__ = "company1"
    id = db2.Column(db2.Integer, primary_key = True)
    name = db2.Column(db2.Text, nullable = False)
    mobile = db2.Column(db2.Integer, nullable = False)
    email = db2.Column(db2.Text, nullable= False)
    can_email= db2.Column(db2.Integer, nullable=False)
    can_mobile= db2.Column(db2.Integer, nullable=False)

class company2(db2.Model):
    __tablename__ = "company2"
    id = db2.Column(db2.Integer, primary_key = True)
    name = db2.Column(db2.Text, nullable = False)
    mobile = db2.Column(db2.Integer, nullable = False)
    email = db2.Column(db2.Text, nullable= False)
    can_email= db2.Column(db2.Integer, nullable=False)
    can_mobile= db2.Column(db2.Integer, nullable=False)

class company3(db2.Model):
    __tablename__ = "company3"
    id = db2.Column(db2.Integer, primary_key = True)
    name = db2.Column(db2.Text, nullable = False)
    mobile = db2.Column(db2.Integer, nullable = False)
    email = db2.Column(db2.Text, nullable= False)
    can_email= db2.Column(db2.Integer, nullable=False)
    can_mobile= db2.Column(db2.Integer, nullable=False)

db2.create_all()

@app.route("/")
def home():
    return render_template("index.html")

<<<<<<< HEAD
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cname = request.form.get("cname")
        password = request.form.get("password")
        ename = request.form.get("ename")
        print(cname, password, ename)

    return render_template("test.html")

# @app.route("")
=======

@app.route("/login")
def login():

    return render_template("login.html")
>>>>>>> 094dab91a4485b204c2e48e21082c10e4a75d92d


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