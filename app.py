import os

from cs50 import SQL
from flask import Flask, url_for, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/brew", methods=["POST"])
def brew():
    tea_choice = request.form.get("tea")
    image_path = url_for('static', filename=f'{tea_choice}.jpg')
    return render_template("brew.html", tea=tea_choice, image_path=image_path)
