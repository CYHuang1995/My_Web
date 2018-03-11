from flask import Flask
from flask import render_template

app=Flask(__name__)

#指定当浏览器浏览到根地址时接下来要启用的函数是什么
@app.route('/')
def hello():
    return '欢迎光临，你好！'

#指定当浏览器浏览到根地址加上about时接下来要启用的函数是什么
@app.route('/about')
def about():
    return '这是一个使用Flask建立的小网站测试'

#示例：http://127.0.0.1:5000/user/Tom
@app.route('/user/')
@app.route('/user/<username>')
def show_user(username=None):
    return render_template('show_user.html',name=username)

if __name__=='__main__':
    app.run()
