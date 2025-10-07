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


@app.route("/" , methods=['GET', 'POST'])
def response():
    if not session.get('username'):
        return redirect('/login')
    return render_template( 'response.html' )


@app.route("/login"  , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['username'] = None
    return render_template('logout.html')
    
    
if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run(port=3000)
