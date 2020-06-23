from flask import Flask, render_template, request, session

import authentication

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@authentication.authenticate
def hello_world():
    # Return this to the user who visited this page. The browser will render it.
    return f'Hello {authentication.get_actual_user_data()}!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return authentication.verify_password(request.form['email'], request.form.get('password'), app)
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
