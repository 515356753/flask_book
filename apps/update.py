from flask import Blueprint, render_template, request, session, redirect, url_for  # redirect ,url_for重定向跳转
from .models import Books
import config
from config import *
from flask_wtf.csrf import generate_csrf
update = Blueprint('update', __name__)


@update.route('/<id>', methods=["POST", "GET"])
def index(id):
    if request.method == 'POST':
        get_upname = request.form.get('up_name')
        i = Books.query.filter(Books.name == id)
        i.update({'name': get_upname})
        db.session.commit()

    return render_template('ubdate.html')

