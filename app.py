from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitness.db"
db = SQLAlchemy(app)


class Villain(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(250), unique=False, nullable=False)
  interests = db.Column(db.String(250), nullable=False)
  url = db.Column(db.String(250), nullable=False)
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return f"{self.name}: villain"

# newVillain = Villain(name="test", description="test_descr")
# db.session.add(newVillain)
# db.session.commit()

# search = Villain.query.filter_by(name="test".first())
# searchAll = Villain.query,all()
# print(search)
# print(searchAll)

#  delete_test = query.filter_by(name="test")
# if delete_test:
#     db.session.delete(delete_test)
#     db.session.commit()

# def villain_data():
#   username = request,form.get("username")
#   email = request.form.get("email")
#   password = request.form.get("password")

# villain_attributes = request.form.get("favourite_villain")

# villain_form = Villain.query.filter_by(username=username).first()

with app.app_context():
  db.create_all()
  db.session.commit()

@app.route("/") 
def villain_cards():
  return render_template("villain.html", villains=Villain.query.all())

@app.route("/add", methods=["GET"])
def add_villain():
  return render_template("addvillain.html", errors=[])

@app.route("/addVillain", methods=["POST"])
def add_user():
  errors = []
  name = request.form.get("name")
  if not name:
    errors.append("Uh oh! A name is required, please enter one")
  description = request.form.get("description")
  if not description:
    errors.append("Uh oh! Looks like you forgot a description")
  interests = request.form.get("interests")
  if not interests:
    errors.append("Uh oh! Looks like you forgot an interest!")
  url = request.form.get("url")
  if not url:
    errors.append("Uh oh! Looks like you forgot an image!")

  villain = Villain.query.filter_by(name=name).first()
  if villain:
    errors.append("Looks like this villain has already been added!")
  if len(errors) > 0:
    return render_template("addvillain.html", errors=errors)
  else:
    new_villain = Villain(name=name,
                          description=description,
                          interests=interests,
                          url=url)
    db.session.add(new_villain)
    db.session.commit()
    return render_template("villain.html", villains=Villain.query.all())

@app.route("/delete", methods=["DELETE"])
def delete_villain():
  return render_template("deletevillain.html", errors=[])

@app.route("/deleteVillain", methods=["POST"])
def delete_user():
  errors = []
  name = request.form.get("name")
  if villain:
    villain = Villain.query.filter_by(name=name).first()
    if villain:
      db.session.delete(villain)
      db.session.commit()
      return render_template("deletevillain.html", villains=Villain.query.all())
  else:
    return render_template("deletevillain.html", errors=["Villain does not exist! Uh oh!"])

def hello_world():
  return render_template("villain.html")


app.run(host='0.0.0.0', port=8080)
