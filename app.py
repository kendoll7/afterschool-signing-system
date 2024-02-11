from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)

def write_to_csv(username, password):
    with open('user_credentials.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'username': username, 'password': password})

@app.route('/signup', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        write_to_csv(username, password)
        return 'Sign up successful!'
    else:
        return 'Invalid request method'

@app.route('/')
def index():
    return render_template_string('''
        <h1>Sign Up Form</h1>
        <form action="/signup" method="post">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Sign Up</button>
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
