from flask import *
from flask_sqlalchemy import SQLAlchemy


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


account_sid = 'AC99d7765d763b3d0eddb60b19a0f62d27'
auth_token = '6283be6e913eb4223ac51f3eb7b5dbb6'
client = Client(account_sid, auth_token)
def sendMessage(name,phno):
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body="Hey {}!\nYour periods are on the way\n\nItems you might need:\n\nhttps://www.bigbasket.com/pc/beauty-hygiene/feminine-hygiene/tampons-menstrual-cups/\n\nhttps://www.stayfree.in/products\n\nhttps://www.bigbasket.com/ps/?q=period%20heat%20pack&nc=pscs#!page=1".format(name),
    to="whatsapp:+91{}".format(phno)
    )
    print("message sent")
#sendMessage("dominic",6305461499)


def daysCal(datelist):
    datelist = [datetime.strptime(d, '%Y-%m-%d') for d in datelist]
    # calculate the total number of days between all dates
    num_days = list()
    for i in range(len(datelist) - 1):
        delta = datelist[i+1] - datelist[i]
        num_days.append(str(delta).split(" ")[0])
    return num_days

def calPdate(datelist):
    datelist = [datetime.strptime(d, '%Y-%m-%d') for d in datelist]
    # calculate the total number of days between all dates
    num_days = 0
    for i in range(len(datelist) - 1):
        delta = datelist[i+1] - datelist[i]
        num_days += delta.days
    # calculate the average number of days between all dates
    avg_days = num_days / (len(datelist) - 1)
    # define the starting date
    start_date = datelist[-1]
    # calculate the ending date
    end_date = start_date + timedelta(days=avg_days)
    end_date=str(end_date).split(" ")[0]
    #print("Predicted date = ",end_date) # output: 2023-03-22 00:00:00
    return end_date


#Scheduler
def action():
    print("Scheduler is working")
    with app.app_context():
        results = User.query.filter_by(pdate=str(dt.date.today())).all()
    for result in results:
        sendMessage(result.name,result.phno)
    print("Sent")

"""def test():
    #app.app_context().push()
    with app.app_context():
        results = User.query.filter_by(name="asd").all()
    a=list()
    for i in results:
        a.append(i.name)
    print(a)
    return a"""

scheduler = BackgroundScheduler()
scheduler.add_job(action, 'interval', seconds=5)
scheduler.start()


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