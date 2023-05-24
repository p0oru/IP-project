from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = '12eip'

# Initialize MySQL
mysql = MySQL(app)
app.secret_key = b'/\x14\xd0\xf3$e^\xc5\x19\xd0\xdf\xb5\x91#\x9d\x81\x94t\xc7r\x98\x9f\xee\xba'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/templates/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_credentials(username, password):
            # Perform login operation (e.g., set session, redirect to dashboard, etc.)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


def check_credentials(username, password):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM data WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    app.run(debug=True)