from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return f'Print User-Agent : {user_agent}'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/bug')
def bug():
    bug = 5/0
    return 'buggy world'

@app.route('/re')
def re():
    return redirect('http://www.naver.com')

if __name__ == '__main__':
    print(app.url_map)
    app.run()