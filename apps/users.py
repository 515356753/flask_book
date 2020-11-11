from flask import Blueprint, render_template, request, session, redirect, url_for  # redirect ,url_for重定向跳转
users = Blueprint('users', __name__)  #模块名/蓝图名叫users


@users.route('/')     # 路由定义!
def index():
    return render_template('index.html')  # 跳转到模板!





