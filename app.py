from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
    host= "172.27.179.8",
    user="root",
    password="Shanks@2003",
    port='3306',
    database="test_K8s"  # Specify the database name here
)
def create_table() :
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), age INT(3),  grade INT(3))")
    cursor.close()

def insert_data(name, age, grade):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) ", (name, age, grade))
    mydb.commit()
    cursor.close()

@app.route('/')
def home():
    return redirect('/index')


@app.route('/index', methods = ["POST", "GET"])
def index():
    create_table()
    if request.method == "POST" :
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        insert_data(name, age, grade)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)