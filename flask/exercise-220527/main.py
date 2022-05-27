from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']= 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('go')

@app.route('/form1')
def form1():
    return render_template('form1.html')

@app.route('/form2')
def form2():
    a_form = NameForm()
    return render_template('form2.html', form = a_form)

@app.route('/form3', methods=['GET', 'POST'])
def form3():
    a_name = None
    a_form = NameForm()

    if a_form.validate_on_submit():
        a_name = a_form.name.data
        a_form.name.data = ''
    
    return render_template('form34.html', form = a_form, name = a_name)

@app.route('/form4', methods=['GET', 'POST'])
def form4():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('form4'))
    
    return render_template('form34.html', form = form, name = session.get('name'))

@app.route('/', methods=['GET', 'POST'])
def form5():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        
        session['name'] = form.name.data
    
    return render_template('form5.html', form = form, name = session.get('name'))

if __name__=='__main__':
    app.run()