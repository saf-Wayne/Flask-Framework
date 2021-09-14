from flask import Blueprint, render_template

path = Blueprint(__name__, 'path')

@path.route('/')
def home():
    return render_template('index.html')