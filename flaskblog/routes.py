from flask import render_template, flash, redirect, url_for
from flaskblog import app, db, bcrypt 
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post




posts = [
    {
        'author' : 'Sudhanshu Joshi',
        'title' : 'First Blog',
        'content' : 'First Content',
        'date_posted' : 'April 20, 2020'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Second Blog',
        'content' : 'Second Content',
        'date_posted' : 'April 21, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('About.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful', 'danger')
                
    return render_template('login.html', title='Login', form=form)