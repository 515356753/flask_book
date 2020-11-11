from config import db # 导入数据库对象
from datetime import datetime

# 用户模型(id,name,pwd,phone,email,addr,创建时间)
class Users(db.Model):
    __tablename="users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False,index=True,unique=True) #不为空,索引加快访问速度,名字唯一
    pwd = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    addr = db.Column(db.String(20)) #地址
    create_time = db.Column(db.DATE,default=datetime.now())  # 时间默认为系统当前日期

    def __str__(self):
        return f'名字:{self.name},电话:{self.phone}'


# 作者
class Author(db.Model):
    __tablename = "author"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, index=True, unique=True)  # 不为空,索引加快访问速度,名字唯一

    # 1方配置关系,配置反向引用的名字
    books = db.relationship('Books',backref='author')



# 书籍(id,名字,价格,作者id,出版日期)
class Books(db.Model):
    __tablename = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, index=True, unique=True)  # 不为空,索引加快访问速度,名字唯一

    # 多方外键:  书籍.author.作者名字
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))#或Author.id