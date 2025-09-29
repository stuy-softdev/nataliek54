# Natalie Keiger
# SoftDev
# September 2025

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #prints to terminal
    return "No hablo queso!"

app.run()

