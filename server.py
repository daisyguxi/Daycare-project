"""Server for daycares app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud, os, requests
from pprint import pprint
from random import choice
import json

from jinja2 import StrictUndefined
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

YELP_KEY = os.environ['YELP_KEY']



# Replace this with routes and view functions!
@app.route("/")
def homepage():    
    """View homepage."""

    return render_template("homepage.html")


@app.route("/search", methods=['POST'])
def search():
    """Search for daycares on Yelp"""
    postalcode = request.form.get('postalcode')
    url = "https://api.yelp.com/v3/businesses/search"
    auth = {'Authorization': 'Bearer %s' % YELP_KEY}
    payload = {'limit': '30', 'location': postalcode, 'categories': 'childcare'}
    data = requests.get(url, params=payload, headers=auth).json()
    age_low = ['0.5Y', '1Y'] 
    age_high = ['3Y', '4Y', '5Y']
    languages1 = 'English'
    languages2 = ['Mandarin', 'Spanish']

    potty = ["Yes", "No"]
    monthly_fee = ["$1200", "$1300", "$1400", "$1500", "$1600", "$1700", "$1800", "$1900", "$2000"]

    fake_data = []
    for i in range(len(data['businesses'])):
        business_copy = {}
        Low = choice(age_low)
        High = choice(age_high)
        Language1 = languages1
        Language2 = choice(languages2)
        Potty = choice(potty)
        Monthly_fee = choice(monthly_fee)
        business_copy["age_low"] = Low
        business_copy["age_high"] = High
        business_copy["languages1"] = Language1
        business_copy["languages2"] = Language2
        business_copy["potty"] = Potty
        business_copy["monthly_fee"] = Monthly_fee
        fake_data.append(business_copy)


    #build new keys, then add to fake_data
    #len(data.business)
    #in the loop, create fake data, choice in age low, age high...
    #age_low =low, age_high= high, then input to the dictionary fake_data
    #inside item 0 we have low =2, high=5
    #value1 is dictionary, nest dictinaries

    #data = requests.get(url, params=payload, headers=auth).json()
    
  
    return render_template('daycare.html',
                           businesses=data['businesses'],
                           fake_data=fake_data,
                           length=len(data["businesses"]),
                           postalcode=postalcode)

    
    # print(data)
    # pprint(data['businesses'])
    # return render_template()

# @app.route('/search/business')
# def daycare():
#    """View the details of an event."""

#    url = 'https://api.yelp.com/v3/businesses/search'
#    auth = {'Authorization': 'Bearer %s' % YELP_KEY}

#    payload = {'business': 'businesses'}

#    data = requests.get(url, params=payload, headers=auth).json()
#    business = data['businesses'][0]
    

#    return render_template('daycare.html',
#                            business=business)
#    #return data['businesses']['id']





@app.route("/users", methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    

    if not user:
        flash("Please enter your email address.")
        return redirect("/")
    elif user.password != password:
        flash("Password is incorrect, please try again.")
        return redirect("/")
    
    
    return render_template('users.html')
        



@app.route("/signup", methods=['POST'])
def signup():
    return render_template('signup.html')

@app.route("/signin", methods=['POST'])
def signin():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    zipcode = request.form.get('zipcode')
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)
    print(user)

    if user:
        flash("There is an existing account associated with this email. Please sign in.")

    else:
        user = crud.create_user(fname, lname, zipcode, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please sign in.")

    
    return redirect("/")


# @app.route("/daycare", methods=['POST'])
# def daycare():
#     name = request.form.get('name')
#     phone = request.form.get('phone')
#     location = request.form.get('location')
#     image = request.form.get('image')


#     return render_template('daycare.html',
#                             name=name,
#                             phone=phone,
#                             location=location,
#                             image=image)
@app.route('/daycare_detail')
def daycareDetail():
    #address = request.form.get('city')
    #phone = request.form.get('phone')
    name = request.args.get('name')
    zipcode = request.args.get('zipcode')
    fakedata = request.args.get('fakedata')
    fakedata = fakedata.replace("\'", "\"")
    fakedata = json.loads(fakedata)



    url = "https://api.yelp.com/v3/businesses/search"
    auth = {'Authorization': 'Bearer %s' % YELP_KEY}
    payload = {'limit': '1', 'location': zipcode, 'term': name}
    
    #print(name)
    print(fakedata)
    print("\n"*5)
    print(type(fakedata))

    data = requests.get(url, params=payload, headers=auth).json()
    #print(data, 'LINE 169 DATA')
    return render_template('saveandcontact.html',
                           data=data,
                           fake_data=fakedata)
    
    #return data


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
