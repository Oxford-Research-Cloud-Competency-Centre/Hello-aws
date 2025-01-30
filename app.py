# © The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved

from flask import Flask, render_template

app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    return render_template("index.html")