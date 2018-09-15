# -*- coding:utf-8 -*-
from flask import Flask,request,url_for,render_template
from models import User

app = Flask(__name__)

@app.route('/')
def hello():
    content = "hello,xiaoya"
    return render_template("index.html", content=content)

@app.route('/user')
def user():
    user = User(1,'xiaoyan')
    return render_template('user_index.html', user=user)

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) ==1:
        user = User(1,'xiaoyan')
    return render_template("user_id.html", user=user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        u = User(i, 'user:'+str(i))
        users.append(u)
    return render_template('user_list.html', users=users)

@app.route('/one')
def one():
    return render_template("one_base.html")

@app.route('/two')
def two():
    return render_template("two_base.html")


# @app.route('/hello world')
# def hello_world():
#     return '<h1>Hello World!</h1>'
#
# @app.route('/user', methods=['POST'])
# def hello_user():
#     return 'hello,user!'
#
# @app.route('/users/<id>')
# def user_id(id):
#     return 'hello user:'+id
#
# @app.route('/query_user')
# def query_user():
#     id = request.args.get('id')
#     return 'query user:'+id
#
# @app.route('/query_url')
# def query_url():
#     return 'query urll:'+url_for('query_user')


if __name__ == '__main__':
    app.run()
