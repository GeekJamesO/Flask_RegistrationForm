from flask import Flask, request, render_template, flash
import re

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
    password1 = request.form['password1']
    password2 = request.form['password2']

    validated = True

    if (len(email) < 1):
        validated = False
        flash("email must not be blank!", "error")
    elif not EMAIL_REGEX.match(email):
        validated = False
        flash("'{}' is an invalid Email Address!".format(email), "error")
    else:
        print "Email is good"

    if (len(first_name) < 1):
        validated = False
        flash("First Name must not be blank!", "error")
    elif (any(char.isdigit() for char in first_name)):
        validated = False
        flash("'{}' numbers are not allowed in first name!".format(first_name), "error")
    else:
        print "First Name is good"

    if (len(last_name) < 1):
        validated = False
        flash("Last Name must not be blank!", "error")
    elif (any(char.isdigit() for char in last_name)):
        validated = False
        flash("'{}' numbers are not allowed in last name!".format(last_name), "error")
    else:
        print "Last Name is good"

    if (len(password1) < 8):
        validated = False
        flash("First Password must not be atleast 8 characters!", "error")

    if (len(password2) < 8):
        validated = False
        flash("Second Password must not be atleast 8 characters!", "error")

    if (password1 != password2):
        validated = False
        flash("Passwords do not match!", "error")

    if (validated):
        return render_template('Success.html')
    else:
        return render_template('index.html')

app.run(debug=True)
