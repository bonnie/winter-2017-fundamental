from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

# create app
app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route('/')
def home():
    """display home page"""

    return render_template("login.html")


@app.route('/process_login', methods=['POST'])
def process_login():
    """receive and evaluate login information"""

    email = request.form.get('email_name')
    password = request.form.get('password_name')

    # replace with some searching in database to get userID
    if email == 'balloonicorn@hackbrightacademy.com' and \
        password == 'sparkles': 
            session['user_id'] = 4
            message = "logged in"
    else:
        message = "not logged in"

    return render_template("login_confirm.html",
                            login_message=message)

@app.route("/super_secret")
def display_secret_info():
    """display secret info if logged in."""

    return render_template("secret_info.html")


@app.route("/change_password", methods=["POST"])
def change_password():
    """change user password"""

    oldpass = request.form.get('old')
    newpass = request.form.get('new')

    print "old pass", oldpass
    print "new pass", newpass

    return 'success Ashley!'


if __name__ == "__main__":

    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    app.run(host="0.0.0.0")
