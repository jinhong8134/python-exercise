from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/template/<name>')
def user_template(name):
    name = '<h1>h1 tag test</h1>'
    return render_template('user.html', name = name)

@app.route('/template/safe')
def user_template_safe():
    name = '<h1>h1 tag test</h1>'
    return render_template('safe.html', name = name)

@app.route('/ext')
def user_template_extend():
    return render_template('extend.html')

if __name__ == '__main__':
    app.run()