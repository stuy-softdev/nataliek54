import random
import numpy as np

def choose_career(filename):
    file = open(filename, "r")
    content = file.read().strip().split("\n")
    career_dict = {}
    num = random.randint(0, len(content) - 2)
    for i in range(1, len(content) - 1):
        line = content[i].rsplit(",", 1)
        if "," in line[0]:
            career_dict[line[0][1:-1]] = float(line[1])
            if i == num:
                career_dict[line[0][1:-1]] = career_dict[line[0][1:-1]] + 0.2
        else:
            career_dict[line[0]] = float(line[1])
            if i == num:
                career_dict[line[0]] = career_dict[line[0]] + 0.2
             
    #random choice
    keys = list(career_dict.keys())
    vals = list(career_dict.values())
    vals = [x/100 for x in vals]
    randomoccupation = np.random.choice(keys, size=1, p=(vals))[0]
    print(randomoccupation, career_dict[randomoccupation] - 0.2)
    return randomoccupation + ", " + str(round(career_dict[randomoccupation] - 0.2, 3))

choose_career('occupations.csv')