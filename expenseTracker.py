from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to your existing MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1:3306",
        user="root",
        password="Vandita@2801",
        database="banks"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transcations")
    all_expenses = cursor.fetchall()
    conn.close()
    return render_template('index.html', transcations=all_expenses)

@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']
    amount = request.form['amount']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (item_name, amount) VALUES (%s, %s)", (item, amount))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)