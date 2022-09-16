"""CRUD operations."""
from model import db, User, Daycare, Save, connect_to_db

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
    
def create_daycare(name, phone, rating, address, min_age, max_age, language1, language2, potty, monthly_fee):
    """Create and return a new daycare"""
    daycare = Daycare(
        name=name,
        phone=phone,
        rating=rating,
        address=address,
        min_age=min_age,
        max_age=max_age,
        language1=language1,
        language2=language2,
        potty=potty,
        monthly_fee=monthly_fee
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

def create_save(user, daycare):
    save = Save(user=user, daycare=daycare)
    db.session.add(save)
    db.session.commit()
    return save

def get_saves_by_user(user):
    user_id = user.user_id
    return Save.query.filter(Save.user_id == user_id).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app) 