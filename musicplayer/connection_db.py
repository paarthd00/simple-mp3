# connection_db.py
# To initialize the DB
# Change connection conn Db path ../Db/app.db
# and run this file
import sqlite3
from datetime import date

today = date.today()
today = str(today)
conn = sqlite3.connect('./Db/app.db')

cur = conn.cursor()


def delete_song(song_name):
    sql = '''DELETE FROM songs WHERE name=?'''
    cur.execute(sql, (song_name,))
    conn.commit()
    return 1


def delete_collection(_id):
    sql = '''DELETE FROM collections WHERE group_id=?'''
    cur.execute(sql, (_id,))
    conn.commit()
    return 1


def insert_song(music):
    sql = ''' INSERT INTO songs(group_id,date,name,artist,url)
              VALUES(?,?,?,?,?) '''

    cur.execute(sql, music)

    conn.commit()
    return cur.lastrowid


def insert_collection(collection):
    sql = ''' INSERT INTO collections(date,name)
              VALUES(?,?) '''

    cur.execute(sql, collection)

    conn.commit()
    return cur.lastrowid


def show_music(table_name, group_id):
    cur.execute(" SELECT * from " + table_name + " WHERE group_id=?", str(group_id))
    data = cur.fetchall()
    conn.commit()
    for el in data:
        print(el)
    return data


def show_collections(table_name):
    cur.execute("SELECT * from " + table_name)
    data = cur.fetchall()
    for el in data:
        print(el)
    return data


def get_collection_name(_id):
    sql = '''SELECT name FROM collections WHERE group_id=?'''
    cur.execute(sql, (_id,))
    name = cur.fetchone()
    name = ''.join(name[0])
    return name


def get_url(name):
    cur.execute("SELECT url from songs WHERE name=?", (name,))
    data = cur.fetchall()
    return data


def create_tables():
    sql = ['''CREATE TABLE if not exists songs (group_id INTEGER NOT NULL, date text, name text NOT NULL PRIMARY KEY,
     artist text, url text, FOREIGN KEY (group_id) REFERENCES supplier_groups (group_id))''',
           '''CREATE TABLE if not exists collections
                           ( group_id INTEGER PRIMARY KEY AUTOINCREMENT, date text, name text)'''
           ]
    for el in sql:
        cur.execute(el)
    conn.commit()

    return 1


def main():
    create_tables()
    music_list = [(1, today, 'FireSquad', 'rap', "https://www.youtube.com/watch?v=HCURqfqL8sI"),
                  (1, today, 'Skegee', 'rap', "https://www.youtube.com/watch?v=z6RlzkWY2o4"),
                  (1, today, 'GangSigns', 'rap', "https://www.youtube.com/watch?v=_WnXMMOkubA"),
                  (2, today, 'letitbreathe', 'lofi', "https://www.youtube.com/watch?v=0WGPP_3BPPQ"),
                  (2, today, 'trustnobody', 'lofi', "https://www.youtube.com/watch?v=XuSFWY_7e54")]
    collections = [(today, 'rap'), (today, 'lofi')]
    for c in collections:
        insert_collection(c)
    for el in music_list:
        insert_song(el)
    show_collections("collections")
    conn.close()


if __name__ == '__main__':
    main()

# choose online
# shows all the online collections
# options for the online collections
# chooses options, and perform action from the local sql db
# takes the user to online source

