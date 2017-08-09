from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = "ThisSoundBeSuperSpecialAndSecret"

@app.route('/', methods=['GET'])
def  RegistrationForm():
    return render_template('index.html')

@app.route('/process', methods=['GET'])
def  process():

    if (TRUE):
        return render_template('Success.html')
    else:
        return render_template('index.html')



app.run(debug=True)
