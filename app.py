from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registered_users = []

@app.route('/')
def index():
    return render_template('registration_form.html')

@app.route('/register', methods = ['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return 'Моля, попълнете всички полета'

    registered_users.append({'username': username, 'password': password})
    return 'Регистрацията е успешна'

if __name__ == '__main__':
    app.run(debug=True)