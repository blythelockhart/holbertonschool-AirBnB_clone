#!/usr/bin/python3
"""sets up unique instance of FileStorage"""


from models.engine import file_storage


# makes storage, an instance of FileStorage
storage = file_storage.FileStorage()
# storage instance is initialized with data from the JSON file (if it exists)
storage.reload()
