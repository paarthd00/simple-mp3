import sqlite3
conn = sqlite3.connect('../Db/app.db')


create_table_queries = [
    "CREATE TABLE if not exists music_player (date text, name text, artist text, album text)",
]
fill_tables_queries = []
drop_tables_queries = []
cur = conn.cursor()

cur.execute('''CREATE TABLE if not exists music_player
            (date text, name text, artist text, album text)''')

cur.execute('''CREATE TABLE if not exists music_player
            (date text, name text, artist text, album text)''')

conn.commit()

conn.close()
