"""CRUD operations."""
from model import db, User, Daycare, Appointment, Save, connect_to_db

"""Functions start here!"""

def create_user(first_name, last_name, zip_code, email, password ):
    """Create and return a new user"""

    user = User(first_name=first_name,
           last_name=last_name,
           zip_code=zip_code,
           email=email,
           password=password
    )
    return user

def get_users():
    """Return all users."""
    return User.query.all()


def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()
    
def create_daycare(daycare_name, kid_age_low, kid_age_high, monthly_fee, languages, potty_train, zip_code):
    """Create and return a new daycare"""
    daycare = Daycare(
        daycare_name=daycare_name,
        kid_age_low=kid_age_low,
        kid_age_high=kid_age_high,
        monthly_fee=monthly_fee,
        languages=languages,
        potty_train=potty_train,
        zip_code=zip_code
    )
def get_daycares():
    """Return all daycares."""
    return Daycare.query.all()

def get_daycare_by_id(daycare_id):
    """Return a daycare by primary key."""
    return Daycare.query.get(daycare_id)

def create_appointment(user, daycare, appt_time):
    """Create and return a new appointment"""
    appointment = Appointment(user=user, daycare=daycare, appt_time=appt_time)
    return appointment

def update_appointment(appt_id, new_appt_time):
    """Update an appointment given appt_id and the updated appt_time."""
    appointment = Appointment.query.get(appt_id)
    appointment.appt_time = new_appt_time

def create_save(user, daycare):
    save = Save(user=user, daycare=daycare)
    return save


if __name__ == '__main__':
    from server import app
    connect_to_db(app)