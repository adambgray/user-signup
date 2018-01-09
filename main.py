from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():
    error_name = ''
    error_password = ''
    error_email = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        
        if len(username) < 3 or len(username) > 20:
            error_name = 'Username must be between 3 and 20 characters with no spaces.'
        
        if ' ' in username:
            error_name = 'Username must not contain spaces.'

        if password != verify:
            error_password = 'Password and confirmation must match'
        
        if len(password) <3 or len(password) > 20:
            error_password = 'Password must be between 3 and 20 characters with no spaces.'
        
        if ' ' in password:
            error_password = 'Password must not contain spaces.'

        if email:
            if not re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
                error_email = 'Email address must contain an @ and a .'

        if error_name or error_password or error_email:
            return render_template('index.html',error_name=error_name,
                                   error_password=error_password,
                                   error_email=error_email,
                                   email=email,
                                   username=username)
        else:
            return render_template('welcome.html',
                                    username=username)

        

    else:    
        return render_template('index.html')

if __name__ == '__main__':
    app.run()