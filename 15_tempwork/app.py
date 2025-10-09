from flask import Flask, render_template
app = Flask(__name__)

import random
import numpy as np

coll = []

file = open("data/occupations.csv", "r")
content = file.read().strip().split("\n")
career_dict = {}
num = random.randint(0, len(content) - 2)
for i in range(1, len(content) - 1):
    line = content[i].rsplit(",", 2)
    if "," in line[0]:
        career_dict[line[0][1:-1]] = [float(line[1]), line[2]]
        if i == num:
            career_dict[line[0][1:-1]] = [career_dict[line[0][1:-1]][0] + 0.2, career_dict[line[0][1:-1]][1]]
    else:
        career_dict[line[0]] = [float(line[1]), line[2]]
        if i == num:
            career_dict[line[0]] = [career_dict[line[0]][0] + 0.2, career_dict[line[0]][1]]
keys = list(career_dict.keys())
vals = []
for val in list(career_dict.values()):
    vals.append(val[0])
links = []
for link in list(career_dict.values()):
    links.append(link[1])
    
for i in range(len(keys)):
    coll.append([keys[i], vals[i], links[i]])

def choose_career():
    keys = list(career_dict.keys())
    vals = []
    for val in list(career_dict.values()):
        vals.append(val[0])
    #random choice
    vals = [x/100 for x in vals]
    randomoccupation = np.random.choice(keys, size=1, p=(vals))[0]
    return randomoccupation + ", " + str(round(career_dict[randomoccupation][0] - 0.2, 3)) + ", " + career_dict[randomoccupation][1]
        
@app.route("/wdywtbwygp")
def careerChooserWebsite():
    return render_template('tablified.html', chosen=choose_career(), collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()