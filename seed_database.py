"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb daycares')
os.system('createdb daycares')


model.connect_to_db(server.app)
model.db.create_all()

# Load daycare data from JSON file
with open("Data/daycares.json") as f:
    daycare_data = json.loads(f.read())

# Create daycares, store them in list so we can use them
daycares_in_db = []
for daycare in daycare_data:
    name, phone, rating, address, min_age, max_age, language1, language2, potty, monthly_fee = (
        daycare["name"],
        daycare["phone"],
        daycare["rating"],
        daycare["address"],
        daycare["min_age"],
        daycare["max_age"],
        daycare["language1"],
        daycare["language2"],
        daycare["potty"],
        daycare["monthly_fee"]
    )

    db_daycare = crud.create_daycare(name, phone, rating, address, min_age, max_age, language1, language2, potty, monthly_fee)
    daycares_in_db.append(db_daycare)

model.db.session.add_all(daycares_in_db)
model.db.session.commit()

