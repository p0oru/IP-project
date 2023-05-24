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
app.secret_key = 'secret_key'


@app.route('/')
def home():
    return render_template('signup.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        grade = request.form['grade']
        gender = request.form['gender']
        school = request.form['school']
        board = request.form['board']
        
        if insert_data(first_name, last_name, username, password, age, grade, gender, school, board):
            return render_template('signup.html', script="alert('Form submitted successfully!');")
        else:
            return "An error occurred while inserting data."
   

def insert_data(first_name, last_name, username, password, age, grade, gender, school, board):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO data (first_name, last_name, username, password, age, grade, gender, school, board) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, username, password, age, grade, gender, school, board)
        )
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    app.run(debug=True)