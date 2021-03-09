# This is a playlist manager
# @author Paarth
# main.py
import os
from playsound import playsound

path = os.getcwd()

"""
# -----------------------------------------------------------------------------
# display_menu, takes an array and format menu 
# -----------------------------------------------------------------------------
"""


def display_menu(menu_array):
    # Prints menu
    temp_str = ""
    for el in menu_array:
        temp_str += el + "\n"
    print(f"" + temp_str)


"""
# -----------------------------------------------------------------------------
# gets input from menu option and returns the selected option
# @return type int 
# -----------------------------------------------------------------------------
"""


def get_input(menu):
    while 1:
        display_menu(menu)
        val = input("=>choose option:: ")
        try:
            val = int(val)
            if 0 < val <= len(menu):
                return val
        except ValueError:
            print("value error, Choose correct option")


"""
# -----------------------------------------------------------------------------
# Online media player handler, connects to the Db and shows all the collections
# -----------------------------------------------------------------------------
"""


def online_handler():
    print("online handler")


# Offline Handler
# -----------------------------------------------------------------------------


"""
# -----------------------------------------------------------------------------
# displays the directory dir_name 
# -----------------------------------------------------------------------------
"""


def display_all_local_media(dir_name: str):
    arr = os.listdir(str('./musicplayer/media' + dir_name))
    for i in range(len(arr)):
        print("Item {} : {}".format(i+1, arr[i]))
    print("\n")


"""
# -----------------------------------------------------------------------------
# offline_collection_create
# name param passed and creates a new collection 
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------
# offline_collection_open
# show all the songs in a collection
# -----------------------------------------------------------------------------
"""


def offline_collection_open(collection_name):
    try:
        display_all_local_media("/" + collection_name)
        song_int = get_input(["1.Play Song", "2.Delete Song", "3.Update Song"])
        if song_int == 1:
            name_song = input("=>Enter the name of the song:: ")
            temp_song_str = str(path + "/musicplayer/media/" + collection_name + "/" + name_song)
            playsound(temp_song_str)
    except OSError:
        print("can open %s failed" % collection_name)
    else:
        print("Successfully opened %s " % collection_name)


"""
# -----------------------------------------------------------------------------
# offline_collection_delete
# Deletes the selected collection
# -----------------------------------------------------------------------------
"""


def offline_collection_delete(collection_name):
    try:
        temp = path + "/musicplayer/media/" + collection_name
        os.mkdir(temp)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


"""
# -----------------------------------------------------------------------------
# offline_handler
# handles all the requests on local system
# -----------------------------------------------------------------------------
"""


def offline_handler():
    while 1:
        display_all_local_media("/")
        collection_int = get_input(["1.Create new Collection", "2.Open Collection", "3.Delete Collection"])
        name = input("=>Enter the name of collection:: ")
        if collection_int == 1:
            print("create")
            offline_collection_create(name)
        elif collection_int == 2:
            offline_collection_open(name)
            print("open")
        elif collection_int == 3:
            offline_collection_delete(name)
            print("delete")


# ------------------------------------------------


if __name__ == '__main__':
    initial_menu_arr = ["1. Offline", "2. Online"]
    type_int = get_input(initial_menu_arr)
    if type_int == 1:
        offline_handler()
    elif type_int == 2:
        online_handler()
