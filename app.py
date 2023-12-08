from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        return "Username already exists. Please choose a different username."
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(debug=True)
