import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="balkanid",
    user=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD')
)

cur = conn.cursor()

cur.execute(""" 
    CREATE TABLE IF NOT EXISTS owners(
    id INT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    type VARCHAR(100) CHECK(type IN('User', 'Organization')))
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS repos(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    stars INT,
    status VARCHAR(100) CHECK (status IN ('public', 'private')),
    oid INT);
""")

conn.commit()

# cur.close()
# conn.close()
