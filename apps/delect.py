from flask import Blueprint, render_template, request, session, redirect, url_for  # redirect ,url_for重定向跳转
from .models import Books
import config
from config import *
from flask_wtf.csrf import generate_csrf
delect = Blueprint('delect', __name__)