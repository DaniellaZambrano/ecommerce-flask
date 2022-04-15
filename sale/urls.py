from flask import render_template, session, request, redirect, url_for

from sale import app, db

@app.route('/')
def home():
    return "home"

