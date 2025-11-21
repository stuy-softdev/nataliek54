import urllib.request
import json
from flask import Flask, render_template

app = Flask(__name__)    #create Flask object

@app.route("/")
def main_page():

    fi = open('key_nasa.txt', 'r')
    key = fi.read()

    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key) as response:
        response = response.read().decode()
        print(response)
        json_obj = json.loads(response)
        print(json_obj['url'])
        img = json_obj['url']
        desc = json_obj['explanation']

    return render_template('main.html', image=img, exp=desc)

if __name__ == "__main__":
    app.debug = True
    app.run()
