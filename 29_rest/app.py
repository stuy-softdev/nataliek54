import urllib.request
import json
from flask import Flask, render_template

app = Flask(__name__)    #create Flask object

@app.route("/")
def main_page():

    fi = open('key_nasa.txt', 'r')
    key = fi.read()

    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key) as response:
        data = response.read()
        link = reponse[url]
        img = '<img src=' + link + '>'

    return render_template('main.html', image=img)

if __name__ == "__main__":
    app.debug = True
    app.run()
