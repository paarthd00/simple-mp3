import sqlite3
from datetime import date

today = date.today()
today = str(today)
conn = sqlite3.connect('./Db/app.db')

cur = conn.cursor()


def insert_song(conn, music):
    sql = ''' INSERT INTO songs(group_id,date,name,artist,url)
              VALUES(?,?,?,?,?) '''

    cur.execute(sql, music)

    conn.commit()
    return cur.lastrowid


def insert_collection(conn, collection):
    sql = ''' INSERT INTO collections(date,name)
              VALUES(?,?) '''

    cur.execute(sql, collection)

    conn.commit()
    return cur.lastrowid


def show_music(conn, table_name):
    sql = " SELECT * from " + table_name
    data = cur.execute(sql)
    conn.commit()
    for el in data:
        print(el)
    return data


def create_tables(conn):
    sql = ['''CREATE TABLE if not exists songs (group_id INTEGER NOT NULL, date text, name text NOT NULL PRIMARY KEY, artist text, 
                            url text, FOREIGN KEY (group_id) REFERENCES supplier_groups (group_id))''',
           '''CREATE TABLE if not exists collections
                           ( group_id INTEGER PRIMARY KEY AUTOINCREMENT, date text, name text)'''
           ]
    for el in sql:
        cur.execute(el)
    conn.commit()

    return 1


def main():
    create_tables(conn)

    music = (1,today,'Summertime2','Mac',"https://www.youtube.com/watch?v=qL7zrWcv6XY")
    collections = (today, 'Mac')
    insert_collection(conn, collections)
    insert_song(conn, music)
    show_music(conn, "songs")

    show_music(conn, "collections")

    conn.close()


if __name__ == '__main__':
    main()

# choose online
# shows all the online collections
# options for the online collections
# chooses options, and perform action from the local sql db
# takes the user to online source
#
