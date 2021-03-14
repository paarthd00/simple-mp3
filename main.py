# This is a playlist manager
# @author Paarth
# main.py
import os
import numpy
from playsound import playsound

from musicplayer.connection_db import *


path = os.getcwd()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def display_app():
    print(f"""----------------\n\n|MUSIC MANAGER|\n\n----------------""")


"""
# display_menu, takes an array and format menu 
"""


def display_menu(menu_array):
    # Prints menu
    temp_str = ""
    for el in menu_array:
        temp_str += el + "\n"
    print(f"" + temp_str)


"""
# gets input from menu option and returns the selected option
# @return type int 
"""


def get_input(menu):
    while 1:
        display_menu(menu)
        val = input("=> choose option, to perform action:: ")
        try:
            val = int(val)
            assert isinstance(val, int)
            if 0 <= val < len(menu):
                return val
            elif val >= len(menu):
                print("Value too big")
            elif val < 0:
                print("Negative value")
        except ValueError:
            print("value error, Choose correct option")


def local_music_handler(option: int, collection_name: str):
    if option == 0:
        print("back")
        return
    if option == 4:
        temp = str(path + "/musicplayer/media/" + collection_name)
        os.chdir(temp)
        url = input("Enter the url of youtube video to add as mp3")
        youtube_song = 'youtube-dl -x --embed-thumbnail --audio-format mp3 ' + url
        os.system(youtube_song)
        os.chdir(ROOT_DIR)
        return
    name_song = input("=> Enter the name of the song:: ")
    temp_song_str = str(path + "/musicplayer/media/" + collection_name + "/" + name_song)
    if name_song in os.listdir(str(path + "/musicplayer/media/" + collection_name )):
        if option == 1:
            playsound(temp_song_str)
        elif option == 2:
            os.remove(temp_song_str)
            print(name_song + " deleted!")
        elif option == 3:
            new_song_name = input("enter updated name")
            new_song_str = str(path + "/musicplayer/media/" + collection_name + "/" + new_song_name)
            os.rename(temp_song_str, new_song_str)
    else:
        print("Opps Please check the song name")


"""
# Online media player handler, connects to the Db and shows all the collections
"""
#


def online_handler():
    show_music(conn,"collections",1)
    print("OPTIONS")
    print("-----------")
    collection_int = get_input(["0.Back", "1.Create new Collection", "2.Open Collection", "3.Delete Collection"])
    if collection_int == 2:
        group_id = input("enter group_id")
        show_music(conn,"songs",group_id)
        name_song = input("enter the name of the song")
        temp_url = get_url(conn,name_song)
        new_url = ''.join(temp_url[0])
        # print(new_url)
        os.system(f"mpv " + new_url)
        # insert_collection(conn,collection)
    print(collection_int)
    print("Online Handler")
    pass


# Show all the collections in the Db
# Give options to handle Request
# Take request and perform task


"""
# displays the directory dir_name
"""


def display_all_local_media(dir_name: str):
    arr = os.listdir(str('./musicplayer/media' + dir_name))
    for i in range(len(arr)):
        print("*Item {} : {}".format(i + 1, arr[i]))
    print("\n")


"""
# offline_collection_create
# name param passed and creates a new collection 
"""


def offline_collection_create(name: str):
    try:
        temp = path + "/musicplayer/media/" + name
        os.mkdir(temp)
    except OSError:
        print("Creation of the collection %s failed" % path)
    else:
        print("Successfully created the collection %s " % path)


"""
# offline_collection_open
# show all the songs in a collection
"""


def offline_collection_open(collection_name):
    try:
        display_all_local_media("/" + collection_name)
        song_int = get_input(["0. Back", "1.Play Song", "2.Delete Song", "3.Update Song", "4.mp3 from youtube"])
        local_music_handler(song_int, collection_name)
    except OSError:
        print("can open %s failed" % collection_name)
    else:
        print("Successfully opened %s " % collection_name)


"""
# offline_collection_delete
# Deletes the selected collection
"""


def offline_collection_delete(collection_name):
    try:
        temp = path + "/musicplayer/media/" + collection_name
        os.rmdir(temp)
    except OSError:
        print("Delete directory %s failed" % path)
    else:
        print("Successfully deleted the directory %s " % path)


"""
# offline_handler
# handles all the requests on local system
"""


def offline_handler():
    valid = True
    while valid:
        display_all_local_media("/")

        print("OPTIONS")
        print("-----------")
        collection_int = get_input(["0.Back", "1.Create new Collection", "2.Open Collection", "3.Delete Collection"])

        if collection_int == 0:
            print("back")
            valid = False
            continue
        name = input("=>Enter the name of collection:: ")
        temp_arr = os.listdir(str('./musicplayer/media/'))

        if name in temp_arr:
            if collection_int == 1:
                print("create")
                offline_collection_create(name)
            elif collection_int == 2:
                offline_collection_open(name)
                print("open")
            elif collection_int == 3:
                offline_collection_delete(name)
                print("delete")
        else:
            print("Collection does not exist")


if __name__ == '__main__':
    running = True
    while running:
        display_app()
        initial_menu_arr = ["0. Exit", "1. Offline", "2. Online"]
        type_int = get_input(initial_menu_arr)
        if type_int == 0:
            print("Exiting...")
            running = False
            continue
        elif type_int == 1:
            print(f"\nLooking up local Collections\n------------------------")
            offline_handler()
        elif type_int == 2:
            online_handler()
