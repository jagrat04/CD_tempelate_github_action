from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection parameters
RDS_ENDPOINT = "your-rds-endpoint"  # e.g., mydatabase.cluster-xxxxxx.us-east-1.rds.amazonaws.com
USERNAME = "your-username"           # e.g., admin
PASSWORD = "your-new-password"       # Your RDS password
DATABASE_NAME = "your-database"      # e.g., mydatabase

def create_connection():
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=RDS_ENDPOINT,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE_NAME
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/manhwa', methods=['GET'])
def get_manhwa():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)  # Use dictionary=True to get results as dictionaries
    cursor.execute("SELECT * FROM manhwa")  # Replace with your actual table name
    result = cursor.fetchall()  # Fetch all results
    cursor.close()
    connection.close()
    return jsonify(result)  # Return the results as JSON

@app.route('/manhwa', methods=['POST'])
def add_manhwa():
    new_manhwa = request.json  # Get the JSON data from the request
    title = new_manhwa['title']
    genre = new_manhwa['genre']
    description = new_manhwa['description']

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO manhwa (title, genre, description) VALUES (%s, %s, %s)", 
                   (title, genre, description))
    connection.commit()  # Commit the transaction
    cursor.close()
    connection.close()
    return jsonify({"message": "Manhwa added successfully!"})
@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)    

# if __name__ == '__main__':
#     app.run(debug=True)  # Run the application in debug mode
