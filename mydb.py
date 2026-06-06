import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

try:
    dataBase = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        passwd=os.getenv('DB_PASSWORD'),
    )
    
    cursorObject = dataBase.cursor()
    
    db_name = os.getenv('DB_NAME', 'tech_db')
    
    try:
        cursorObject.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == 1007:
            print(f"Database '{db_name}' already exists.")
        else:
            print(f"Error: {err}")
    
    cursorObject.close()
    dataBase.close()
    
except mysql.connector.Error as err:
    if err.errno == 2003:
        print("Error: Cannot connect to MySQL server. Make sure it's running.")
    elif err.errno == 1045:
        print("Error: Invalid username or password.")
    else:
        print(f"Error: {err}")
except Exception as err:
    print(f"Unexpected error: {err}")
