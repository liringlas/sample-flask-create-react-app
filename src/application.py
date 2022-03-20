from flask import render_template, request, Flask
import os


from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'react-app')
template_dir = os.path.join(template_dir, 'build')

app = Flask(
    __name__, 
    static_url_path='', 
    static_folder=template_dir,
    template_folder=template_dir)

def valid_login(username, password):
    return True

def log_the_user_in(username):
    return True


@app.route("/")
def hello_world():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', error=error)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)