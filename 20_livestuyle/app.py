# Window Dwellers
# Natalie Keiger, Evan Khosh, Veronika Duvanova
# SoftDev 2025
# time spent: 15min
# K20: Serving Looks

from flask import Flask, render_template

app = Flask(__name__)    #create Flask object

@app.route("/")
def main_page():
    return render_template( 'index.html' )

if __name__ == "__main__":
    app.debug = True
    app.run()