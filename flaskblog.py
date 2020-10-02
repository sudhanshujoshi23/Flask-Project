from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4982539fcdd7368bf4fcc579fb9b94c0'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)

