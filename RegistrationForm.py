from flask import Flask, request, render_template, flash
import re
from datetime import date, datetime

app = Flask(__name__)
app.secret_key = "ThisSoundBeSuperSpecialAndSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def  RegistrationForm():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def  process():
    email = request.form["email"]
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birthdate = request.form['birthdate']
    password1 = request.form['password1']
    password2 = request.form['password2']

    isValid = True

    if (len(email) < 1):
        isValid = False
        flash("email must not be blank!", "error")
    elif not EMAIL_REGEX.match(email):
        isValid = False
        flash("'{}' is an invalid Email Address!".format(email), "error")
    else:
        print "Email is good"

    if (len(first_name) < 1):
        isValid = False
        flash("First Name must not be blank!", "error")
    elif (any(char.isdigit() for char in first_name)):
        isValid = False
        flash("'{}' numbers are not allowed in first name!".format(first_name), "error")
    else:
        print "First Name is good"

    if (len(last_name) < 1):
        isValid = False
        flash("Last Name must not be blank!", "error")
    elif (any(char.isdigit() for char in last_name)):
        isValid = False
        flash("'{}' numbers are not allowed in last name!".format(last_name), "error")
    else:
        print "Last Name is good"

    today = date.today()

    print birthdate, "  birthdate"
    # x = datetime.datetime.strptime("2015-01-30", "%Y-%m-%d").strftime("%d-%m-%Y")
    # print "date is ", x
    if(len(birthdate) == 0 ):
        isValid = False
        flash("Birthdate must not be empty!", "error")
    # elif(datetime(birthdate) < today):
    #     isValid = False
    #     flash("Birthdate must not be before today!", "error")
    else:
        print "Birthdate is good"

    if (len(password1) < 8):
        isValid = False
        flash("First Password must not be atleast 8 characters!", "error")
    elif (not any(char.isdigit() for char in password1)):
        isValid = False
        flash("Passwords are required to have atleast one digit!", "error")
    elif (not any(char.isalpha() for char in password1)):
        isValid = False
        flash("Passwords are required to have atleast one letter!", "error")


    if (len(password2) < 8):
        isValid = False
        flash("Second Password must not be atleast 8 characters!", "error")
    elif (not any(char.isdigit() for char in password2)):
        isValid = False
        flash("Passwords are required to have atleast one digit!", "error")
    elif (not any(char.isalpha() for char in password2)):
        isValid = False
        flash("Passwords are required to have atleast one letter!", "error")

    if (password1 != password2):
        isValid = False
        flash("Passwords do not match!", "error")

    if (isValid):
        return render_template('Success.html')
    else:
        return render_template('index.html')

app.run(debug=True)
