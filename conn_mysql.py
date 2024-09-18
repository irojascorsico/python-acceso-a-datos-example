import mysql.connector

conn = mysql.connector.connect(
    user='yourusername',
    password='yourpassword',
    host='yourhost',
    database='yourdbname'
)
cursor = conn.cursor()
