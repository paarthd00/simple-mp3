import sqlite3
from datetime import date

today = date.today()
today = str(today)
conn = sqlite3.connect('../Db/app.db')


create_table_queries = [
    "CREATE TABLE if not exists music_player (date text, name text, artist text, album text)",
]
fill_tables_queries = []
drop_tables_queries = []
cur = conn.cursor()


def insert_music(conn, music):
    sql = ''' INSERT INTO music_player(date,name,artist,album)
              VALUES(?,?,?,?) '''

    cur.execute(sql, music)

    conn.commit()
    return cur.lastrowid


def insert_collection(conn, collection):
    sql = ''' INSERT INTO collections(date,name,songs)
              VALUES(?,?,?) '''

    cur.execute(sql, collection)

    conn.commit()
    return cur.lastrowid


def show_music(conn,table_name):
    sql = " SELECT * from " + table_name
    data = cur.execute(sql)
    conn.commit()
    for el in data:
        print(el)
    return data


def create_tables(conn):
    sql = ['''CREATE TABLE if not exists music_player
                (date text, name text, artist text, album text)''',
           '''CREATE TABLE if not exists collections
                           (date text, name text, songs text)'''
           ]
    for el in sql:
        cur.execute(el)
    conn.commit()

    return 1


def main():
    create_tables(conn)

    # music = (today,'yolo','tolo','best_album')
    collections = (today, 'collection_name', 'tolo')
    insert_collection(conn,collections)
    show_music(conn,"music_player")

    show_music(conn,"collections")

    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()



# choose online
# shows all the online collections
# options for the online collections
# chooses options, and perform action from the local sql db
# takes the user to online source
#


