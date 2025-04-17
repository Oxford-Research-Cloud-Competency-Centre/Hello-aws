# © The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    return render_template("user_interface.html")

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

