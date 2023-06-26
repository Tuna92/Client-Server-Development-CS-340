from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30945
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            if result:
                print("success")
                return True
            else:
                print("failure")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty\n")

# Create method to implement the R in CRUD.
    def read(self, search):
        # search represents our query
        data = list(self.database.animals.find(search))
        return data

# Create method to implement the U in CRUD.
    def update(self, search, update) -> int:
        if search:
            data = self.database.animals.find(search)
            size = len(list(data.clone()))
            if size > 1:
                update_document = self.database.animals.update_many(search, update)
                print("\nmodified animals: ", update_document.modified_count, "\n")
            elif size == 1:
                self.database.animals.update_one(search, update)
                print("\n1 modified animal\n")
            else:
                print("\nno results to update\n")
        else:
            print("\ninvalid search\n")

# Create method to implement the D in CRUD.
    def delete(self, search):
        if search:
            data = self.database.animals.find(search)
            size = len(list(data.clone()))
            
            if size > 1:
                result = self.database.animals.delete_many(search)
                number_removed = result.deleted_count
                print("deleted animals: ", number_removed, "\n")
            elif size == 1:
                self.database.animals.delete_one(search)
                print("1 deleted animal\n")
        else:
            print("invalid search\n")
