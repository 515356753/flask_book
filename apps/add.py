from flask import Blueprint, render_template, request, session, redirect, url_for  # redirect ,url_for重定向跳转
from .models import Books
import config
from config import *
from flask_wtf.csrf import generate_csrf
add = Blueprint('add', __name__)


@add.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        get_name = request.form.get('name')
        i = Books(name=get_name)
        db.session.add(i)
        db.session.commit()
    return render_template('add.html')
