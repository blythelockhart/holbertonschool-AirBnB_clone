#!/usr/bin/python3
"""sets up unique instance of FileStorage"""


from engine import file_storage


# makes storage, an instance of FileStorage
storage = file_storage.FileStorage()
# storage instance is initialized with data from the JSON file (if it exists)
storage.reload()