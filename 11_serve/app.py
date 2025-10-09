# Natalie Keiger
# Salt Lamp Horse
# Softdev
# time taken: 1
# 09-25-25
# K10 -- teardown

'''
DISCO:
* flask is used for terminal things
* flask must be declared as an object(?) on the name of the python file

QCC:
0. in "if __name__ == "__main__" for test cases
1. often used to specify filepaths?
2. prints to the terminal
3. the name of the python file
4. no, nothing is storing the return value
5. java! obj.func() or class.func()
 ...

INVESTIGATIVE APPROACH:
We began discussing immediate observations, then put them together to add onto each other.
We then speculated about gaps in our information.

ERRORS:
 ModuleNotFoundError: No module named 'flask' --> i think i need to download it
'''


from flask import Flask
from career_chooser import *

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():                  # Q2: Where will this print to? Q3: What will it print?
    return str("Salt lamp horse | Names: Natalie Keiger, Evan Khosh, Carrie Ko | " + choose_career('occupations.csv'))           # Q4: Will this appear anywhere? How u know?

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()                             # Q5: Where have you seen similar constructs in other languages?
