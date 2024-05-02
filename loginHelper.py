import hashlib
import mysql.connector
from mysql.connector import Error

# Function to hash strings using SHA-256
def hash_string(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()

pre_hash_username = "User1"
pre_hash_password = "Pass1"

# Hash the username and password
hashed_username = hash_string(pre_hash_username)
hashed_password = hash_string(pre_hash_password)

print(hashed_username)
print(hashed_password)

# Connect to MySQL database
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='University',
                                         user='Henry',
                                         password='Ajnh3nry')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        
        cursor = connection.cursor()

        # Insert user record with hashed values into the users table
        cursor.execute("INSERT INTO users (Username, Password) VALUES (%s, %s)", (hashed_username, hashed_password))
        connection.commit()
        print("User record inserted successfully")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")