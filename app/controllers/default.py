from app import app
import os
from app.models.tables import User
from flask import request, render_template, url_for, jsonify, url_for


@app.route("/")
def index():
    return "Ola Saidino web !"
