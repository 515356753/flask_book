'''
config.py 保存项目配置
'''
from flask import  Flask  # 导入Flask模块
from flask_sqlalchemy import  SQLAlchemy  # 额外安装: 数据库操作模块
from flask_wtf import CSRFProtect  # 额外导入, csrf防护
# 数据库对象
db = SQLAlchemy()


class Config(object):  # 配置类定义Flask项目配置
    WTF_CSRF_CHECK_DEFAULT = False
    '''项目配置信息'''
    DEBUG=True  # 开启调试模式
    # 数据库
    HOSTNAME = "127.0.0.1"
    POST = 3306
    USERNAME = "root"
    PASSWORD = "root"
    DATABASE = "flask_book"

    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, POST,DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SQLALCHEMY_ECHO= True
    SECRET_KEY = "sdfdfdfdxfddesfdgb^$"  # 加密字符串 csrf需要用session也需要用


def create_app():
    '''创建app对象'''
    app =Flask(__name__)
    # 2. 使用csrf保护应用程序
    CSRFProtect(app)
    app.config.from_object(Config)  # 通过配置类加载配置信息
    # 初始化数据库配置
    db.init_app(app)


    #导入蓝图
    from apps.users import users
    from apps.book import book
    from apps.add import add
    from apps.delect import delect
    from apps.update import update
    app.register_blueprint(users, url_prefix="/")  # 用户蓝图/模块
    app.register_blueprint(book, url_prefix="/book")  # 书籍模块
    app.register_blueprint(add, url_prefix="/add")  # 增加书籍
    app.register_blueprint(delect, url_prefix="/delect")  # 删除书籍
    app.register_blueprint(update, url_prefix="/update")  # 修改书籍
    return app


