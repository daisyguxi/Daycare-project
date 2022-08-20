"""Server for daycares app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud, os, requests
from pprint import pprint

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
    
  
    return render_template('daycare.html',
                          data=data)

    
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
    
    user = crud.get_user_by_email('daisy557188@gmail.com')
    print(user)

    if user:
        flash("Cannot create an account with that email. Try again.")

    else:
        user = crud.create_user(fname, lname, zipcode, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    
    return redirect("/")


@app.route("/daycare", methods=['POST'])
def daycare():
    name = request.form.get('name')
    phone = request.form.get('phone')
    location = request.form.get('location')
    image = request.form.get('image')


    return render_template('daycare.html',
                            name=name,
                            phone=phone,
                            location=location,
                            image=image)




   


if __name__ == "__main__":
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)
