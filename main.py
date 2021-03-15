# This is a playlist manager
# main.py
__author__ = "Paarth"
__email__ = "paarthcode@gmail.com"
import os
import sys
from playsound import playsound

from musicplayer.connection_db import *


path = os.getcwd()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def display_app():
    print(f"""----------------\n\n|MUSIC MANAGER|\n\n----------------""")


def display_menu(menu_array):
    """
    display_menu, takes an array and format menu
    :param menu_array:
    :return:
    """
    temp_str = ""
    for el in menu_array:
        temp_str += el + "\n"
    print(f"" + temp_str)


def get_input(menu):
    """
    gets input from menu option and returns the selected option
    :return type int
    """
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


def play_video(song_name):
    """
    Plays the video song_name
    :param song_name:
    :return:
    """
    try:
        temp_url = get_url(song_name)
        new_url = ''.join(temp_url[0])
        os.system(f"mpv " + new_url)
    except ValueError:
        print("song name doesn't exist")


def insert_song(song_name, _id: int):
    """
    inserts a new song song_name to the DB
    :param song_name:
    :param _id:
    :return:
    """
    try:
        url = input("please enter the url")
        collect_name = get_collection_name(_id)
        music_el = (_id, today, song_name, str(collect_name), url)
        insert_song(music_el)
        print("Inserted")
    except Exception as e:
        print("Error: %s" % e)


def online_song_handler(option: int, _id: int):
    """
    handles all the online song requests
    :param option:
    :param _id:
    :return:
    """
    try:
        if option == 0:
            print("back")
        else:
            song_name = input("Enter the name of the song")
            if option == 1:
                play_video(song_name)
            elif option == 2:
                insert_song(song_name, _id)
            elif option == 3:
                delete_song(song_name)
                print("Deleted" + song_name)
    except Exception as e:
        print("Error: %s" % e)


def online_collection_handler(option: int):
    """
    handles all the online collection requests
    :param option: int
    :return:
    """
    try:
        if option == 0:
            print("back")
        elif option == 1:
            collection_name = input("Please enter name for the new collection")
            insert_collection((today, str(collection_name)))
        # open a collection
        elif option == 2:
            group_id = int(input("enter group_id"))
            show_music("songs", group_id)
            # print the menu with options for the songs
            song_int = get_input(["0. Back", "1.Play Song", "2.Insert Song", "3.Delete Song"])
            online_song_handler(song_int, group_id)
        elif option == 3:
            _id = input("Please enter group_id ")
            delete_collection(_id)
        print("Online Handler")
        pass
    except Exception as e:
        print("Error: %s" % e)


def online_handler():
    """
    Online media player handler, connects to the Db and shows all the collections
    :return:
    """
    try:
        print(f"group_id|date|collection_name")
        show_collections("collections")
        print("OPTIONS")
        print("-----------")
        collection_int = get_input(["0.Back", "1.Create new Collection", "2.Open Collection", "3.Delete Collection"])
        online_collection_handler(collection_int)
    except Exception as e:
        print("Error: %s" % e)


def get_song_youtube(collection_name):
    """
    converts youtube video to mp3
    :param collection_name:
    :return:
    """
    try:
        temp = str(path + "/musicplayer/media/" + collection_name)
        os.chdir(temp)
        url = input("Enter the url of youtube video to add as mp3")
        youtube_song = 'youtube-dl -x --embed-thumbnail --audio-format mp3 ' + url
        os.system(youtube_song)
        os.chdir(ROOT_DIR)
    except Exception as e:
        print("Error: %s" % e)


def local_music_handler(option: int, collection_name: str):
    """
    handles all the local song requests
    :param option:
    :param collection_name:
    :return:
    """
    try:
        if option == 0:
            print("back")
            return
        if option == 4:
            get_song_youtube(collection_name)
            return
        name_song = input("=> Enter the name of the song:: ")
        temp_song_str = str(path + "/musicplayer/media/" + collection_name + "/" + name_song)
        if name_song in os.listdir(str(path + "/musicplayer/media/" + collection_name)):
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
    except Exception as e:
        print("Error: %s" % e)


def display_all_local_media(dir_name: str):
    """
    displays the directory dir_name
    :param dir_name:
    :return:
    """
    arr = os.listdir(str('./musicplayer/media' + dir_name))
    for i in range(len(arr)):
        print("*Item {} : {}".format(i + 1, arr[i]))
    print("\n")


def offline_collection_create(name: str):
    """
    offline_collection_create
    name param passed and creates a new collection
    :param name:
    :return:
    """
    try:
        temp = path + "/musicplayer/media/" + name
        os.mkdir(temp)
    except OSError:
        print("Creation of the collection %s failed" % path)
    else:
        print("Successfully created the collection %s " % path)


def offline_collection_open(collection_name):
    """
    offline_collection_open
    show all the songs in a collection
    :param collection_name:
    :return:
    """
    try:
        display_all_local_media("/" + collection_name)
        song_int = get_input(["0. Back", "1.Play Song", "2.Delete Song", "3.Update Song", "4.mp3 from youtube"])
        local_music_handler(song_int, collection_name)
    except OSError:
        print("can open %s failed" % collection_name)
    else:
        print("Successfully opened %s " % collection_name)


def offline_collection_delete(collection_name):
    """
    offline_collection_delete
    Deletes the selected collection
    :param collection_name:
    :return:
    """
    try:
        temp = path + "/musicplayer/media/" + collection_name
        os.rmdir(temp)
    except OSError:
        print("Delete directory %s failed" % path)
    else:
        print("Successfully deleted the directory %s " % path)


def offline_collection_handler(name: str, *temp_arr, collection_int: int):
    """
    Handles offline collection requests
    :param name:
    :param temp_arr:
    :param collection_int:
    :return:
    """
    try:
        if name in temp_arr:
            if collection_int == 1:
                print("collection created")
                offline_collection_create(name)
            elif collection_int == 2:
                offline_collection_open(name)
                print("opened")
            elif collection_int == 3:
                offline_collection_delete(name)
                print("deleted")
        else:
            print("Collection does not exist")
    except Exception as e:
        print("Error: %s" % e)


def offline_handler():
    """
    offline_handler
    handles all the requests on local system
    :return:
    """
    try:
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
            offline_collection_handler(name, temp_arr, collection_int)
    except Exception as e:
        print("Error: %s" % e)


if __name__ == '__main__':
    try:
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
    except Exception as e:
        print("Error: %s" % e)

