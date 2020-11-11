from flask import Blueprint,render_template,request,session,redirect,url_for # redirect ,url_for重定向跳转
from .models import Books,Users
book = Blueprint('book', __name__) #模块名/蓝图名叫users


# 查询
# @book.route('/')     # 路由定义!
# def index():
#     books = Books.query.all()
#     print(books)
#     return render_template('book.html', books=books)


# #后台
@book.route('/list', methods=['GET', 'POST'])     # 路由定义!
def index():
    if request.method == 'GET':
        paginate = Books.query.paginate(1, 3)  # 默认查询第1页
        page = int(request.args.get('page', 1))
        if page < 0:
            page = 1
        if page >= paginate.pages:  # 判断是否大于总页数
            page = paginate.pages
        paginate = Books.query.paginate(page, 3)
        books = paginate.items  # 当前页数据
        return render_template('book.html', books=books, paginate=paginate)  # 跳转到模板!
    else:
        print('模糊查询')
        name = request.form.get('name')  # 书名
        paginate = Books.query.filter(Books.name.like("%"+name+"%")).paginate(1, 3)
        books = paginate.items  # 当前页数据
        return render_template('book.html', books=books, paginate=paginate, name=name)  # 跳转到模板!



