import mysql.connector

# Replace with your database details
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database_name"
}

# Establish a database connection
connection = mysql.connector.connect(**db_config)
