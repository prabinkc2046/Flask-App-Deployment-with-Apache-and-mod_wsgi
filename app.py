# Import necessary libraries
from flask import Flask, render_template, request, redirect
import mysql.connector

# Create a Flask app
app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'your_mysql_host',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'your_database_name',
}

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    username = request.form['username']
    password = request.form['password']

    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert data into the table
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)

        # Commit the changes
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return redirect('/')
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
