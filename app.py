from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from send_notify import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "SDC12345"

# Database Employees
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Employee(UserMixin, db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    company = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Integer, nullable=False)

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable = False)
    mobile = db.Column(db.Integer, nullable = False)
    email = db.Column(db.Text, nullable= False)
    can_email= db.Column(db.Integer, nullable=False)
    can_mobile= db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

def is_admin():
    if current_user.is_admin == 0:
        return False
    else:
        return True

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if not is_admin():
                return abort(403)
            return f(*args, **kwargs)      
        except:
              return abort(403)
    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(user_id)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-customer", methods=["GET", "POST"])
def add_customer():
    if request.method=="POST":
        company = current_user.company
        name = request.form.get("name")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        can_email = request.form.get("canEmail")
        can_mobile = request.form.get("canMobile")
        new_customer = Customer(
            company=company,
            name=name,
            mobile=mobile,
            email=email,
            can_email = int(can_email),
            can_mobile = int(can_mobile)
        )
        db.session.add(new_customer)
        db.session.commit()

@app.route("/read-customers")
def read_customers():
    company = current_user.company
    customers = Customer.query.filter_by(company=company).first()
    return render_template("view-customer.html", customers=customers)

@app.route("/send-notifications", methods=["GET", "POST"])
def send_notifications():
    if request.method == "POST":
        pass

# Login Manager
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        employee = Employee.query.filter_by(email=email).first()
        if employee:
            password = request.form.get("password")
            if employee.password == password:
                login_user(employee)
                return redirect(url_for("home"))

            flash("Invalid password")
            return redirect(url_for("login"))

        flash("User not registered with email!")
        return redirect(url_for("login"))

    return render_template("test.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ename = request.form.get("ename")
        password = request.form.get("password")
        company = request.form.get("company")
        is_admin = request.form.get("is_admin")
        new_employee = Employee(
            ename=ename, 
            password=password, 
            company=company, 
            is_admin=is_admin
        )
        db.session.add(new_employee)
        db.session.commit()
        login_user(new_employee)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)