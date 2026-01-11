import urllib.request
import json
from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/")
def main_page():

    # with urllib.request.urlopen('https://http.cat/100.jpg') as response:
    #     response = response.read().decode()
    #     print(response)
    #     obj = json.loads(response)
    #     img = response[0:len(response)]

    with urllib.request.urlopen('https://dog.ceo/api/breeds/list/all') as response:
        response = response.read().decode()
        breeds = json.loads(response)['message']

    
    return render_template('main.html', breeds=breeds)
                           
                           #imageUrl='https://http.cat/100.jpg')

@app.route("/image")
def image():
    breed = request.args.get('breed')
    print(breed)
    with urllib.request.urlopen(f"https://dog.ceo/api/breed/{breed}/images/random") as response:
        response = response.read().decode()
        img = json.loads(response)['message']

    return render_template('image.html', image=img, breed=breed)

if __name__ == "__main__":
    app.debug = True
    app.run()

# REpresentational State Transfer

# 1. Use HTTP verbs to mean what they do. GET PUT POST DELETE
# 2. Define resources to be URLs (or vice versa).
# 3. Urls like this:
#   http://stars.com/constellations/orion
#   http://stars.com/stars/vega
# HTTP PUT stars.com/stars/mynewstar with parameters {"magnitude": 7.3}


