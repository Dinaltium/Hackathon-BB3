from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# For demonstration purposes, using an in-memory user dictionary.
# In a real application, use a proper database for user management.
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Redirect to the page with the list of items for bidding
            return redirect(url_for('items'))
        else:
            # Add appropriate error handling or message for failed login
            pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Perform validation, check if username already exists, etc.
        # For simplicity, adding the new user to the dictionary
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/items')
def items():
    # This route will display the list of items available for bidding
    # Implement this route according to your requirements
    return render_template('items.html')

if __name__ == '__main__':
    app.run(debug=True)
