from database import create_connection
import os

dbPath = os.getcwd() + "/database/database.db"
conn = create_connection(dbPath)

sql_query = 'INSERT INTO (wid, word) VALUES (1, test)'
conn.execute(sql_query)

sql_query = 'SELECT * FROM words'
conn.execute(sql_query)
conn.close()