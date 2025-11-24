import urllib.request
import json
from flask import Flask, render_template

app = Flask(__name__)    #create Flask object

@app.route("/")
def main_page():

    with urllib.request.urlopen('https://api.weather.gov/alerts') as response:
        response = response.read().decode()
        obj = json.loads(response)
        img = response[0:len(response)]

    return render_template('main.html', image=img)

if __name__ == "__main__":
    app.debug = True
    app.run()
