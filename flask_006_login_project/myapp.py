from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Home', active_page='home')


@app.route('/about')
def about():
    return render_template('about.html', title='About', active_page='about')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', active_page='contact')


@app.route('/register')
def register():
    return render_template('register.html', title='Register', active_page='register')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('admin_success'))
        else:
            return render_template('admin.html', title='Admin', error='Invalid credentials. Please try again.')
    return render_template('admin.html', title='Admin', active_page='admin')


@app.route('/admin_success')
def admin_success():
    return render_template('admin_success.html', title='Admin Success', active_page='admin_success')


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('user_success'))
        else:
            return render_template('user.html', title='User', error='Invalid credentials. Please try again.')
    return render_template('user.html', title='User', active_page='user')


@app.route('/user_success')
def user_success():
    return render_template('user_success.html', title='User Success', active_page='user_success')


if __name__ == '__main__':
    app.run(debug=True)
