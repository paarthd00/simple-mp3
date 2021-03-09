from main import *
import unittest
import os 
from os import path
current_path = os.getcwd()


class OfflineTestMethods(unittest.TestCase):

    def test_online_handler(self):
        self.assertEqual(online_handler(), 'online handler')

    def test_collection_create(self):
        collection_name = "test_collection"
        offline_collection_create(collection_name)
        temp = current_path + "/musicplayer/media/" + collection_name
        self.assertEqual(path.exists(temp), True)

    def test_collection_delete(self):
        collection_name = "test_collection"
        offline_collection_delete(collection_name)
        temp = current_path + "/musicplayer/media/" + collection_name
        self.assertEqual(path.exists(temp), False)


unittest.main()
