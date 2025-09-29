# Natalie Keiger
# SoftDev
# September 2025

from flask import Flask
app = Flask(__name__)          # applies flask to this file

@app.route("/")                # says where it should go file wise
def hello_world():
    print(__name__)            # prints to terminal
    return "No hablo queso!"   # prints in website

app.run()                      # runs program
                
