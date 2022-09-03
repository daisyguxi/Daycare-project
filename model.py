"""Models for Daycare finder app."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30))
    zipcode = db.Column(db.Integer)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"



class Daycare(db.Model):
    """A daycare."""

    __tablename__ = "daycares"

    daycare_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    kid_age_low = db.Column(db.Float, nullable=False)
    kid_age_high = db.Column(db.Float, nullable=False)
    monthly_fee = db.Column(db.Integer, nullable=False)
    languages = db.Column(db.String, nullable=False)
    potty_train = db.Column(db.Boolean)
    zipcode  = db.Column(db.Integer)

    def __repr__(self):
        return f"<Daycare daycare_id={self.daycare_id} name={self.name}>"



class Appointment(db.Model):
    """An appointment."""

    __tablename__ = "appointments"

    appt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    appt_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    daycare_id = db.Column(db.Integer, db.ForeignKey('daycares.daycare_id'))

    user = db.relationship("User", backref="appoitments")
    daycare = db.relationship("Daycare", backref="appointments")

    def __repr__(self):
        return f"<Appointment appt_id={self.appt_id} appt_time={self.appt_time}>"

   


class Save(db.Model):
    """A saved daycare."""
    __tablename__ = "saves"
    save_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    daycare_id = db.Column(db.Integer, db.ForeignKey('daycares.daycare_id'))

   
    user = db.relationship("User", backref="saves")
    daycare = db.relationship("Daycare", backref="saves")


    def __repr__(self):
        return f"<Save save_id={self.save_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///daycares", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

