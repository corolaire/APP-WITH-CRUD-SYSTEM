# its going to contain the connection with database
   #import module to connection
import mysql.connector
#data access to connect to database

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "micaelacorolaire",
    "database": "CRUD_DB"
}

conn = mysql.connector.connect(**db_config)
