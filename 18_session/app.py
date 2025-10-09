# Salt Lamp Horse
# Natalie Keiger, Evan Khosh, Carrie Ko
# SoftDev
# K17: Take and Give
# October 2025
# time taken: 30m

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask, session, redirect             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
#from flask_session import Session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'asdhajskjbweifnoihgis'

@app.route("/")
def main_page():
    if not session.get('username'):
        return '<a href="/login"> Log in here </a>'
    return render_template( 'response.html' )


@app.route("/login" , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/logged_in')
    elif session['username']:
        return redirect('/logged_in')
    return render_template('login.html')

@app.route("/logged_in")
def logged_in():
    return render_template('response.html', user=session['username']) #request.args['username'])

@app.route('/logout')
def logout():
    session['username'] = None
    return render_template('logout.html')
    
    
if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()
