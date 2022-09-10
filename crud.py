"""CRUD operations."""
from model import db, User, Daycare, Appointment, Save, connect_to_db

"""Functions start here!"""

def create_user(fname, lname, zipcode, email, password ):
    """Create and return a new user"""

    user = User(fname=fname,
           lname=lname,
           zipcode=zipcode,
           email=email,
           password=password

    )
    db.session.add(user)
    db.session.commit()
    

    return user

def get_users():
    """Return all users."""
    return User.query.all()


def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()
def get_user_by_password(password):
    return User.query.filter(User.password == password).first()
    
def create_daycare(name, kid_age_low, kid_age_high, monthly_fee, languages, potty_train, zipcode):
    """Create and return a new daycare"""
    daycare = Daycare(
        name=name,
        age_low=age_low,
        age_high=age_high,
        monthly_fee=monthly_fee,
        languages=languages,
        potty=potty,
        zipcode=zipcode
    )

    db.session.add(daycare)
    db.session.commit()

    return daycare

def get_daycares():
    """Return all daycares."""
    return Daycare.query.all()

def get_daycare_by_id(daycare_id):
    """Return a daycare by primary key."""
    return Daycare.query.get(daycare_id)

def create_appointment(user, daycare, appt_time):
    """Create and return a new appointment"""
    appointment = Appointment(user=user, daycare=daycare, appt_time=appt_time)
    db.session.add(appointment)
    db.session.commit()
    return appointment

#def update_appointment(appt_id, new_appt_time):
#    """Update an appointment given appt_id and the updated appt_time."""
#    appointment = Appointment.query.get(appt_id)
#    appointment.appt_time = new_appt_time

def create_save(user, daycare):
    save = Save(user=user, daycare=daycare)
    db.session.add(save)
    db.session.commit()
    return save


if __name__ == '__main__':
    from server import app
    connect_to_db(app)