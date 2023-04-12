import pymongo
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
import random

# Warning : calling DB from outside docker container
def get_db():
    client = MongoClient(host='localhost',
                         port=27018, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["oep_db"]
    return db

# DB
db = get_db()
# Collection : products
products_collection = db.products_tb
# Product (test)
test_product = {"name": "Product test mongo", "description": "Test description.", "size": "medium", "weight": random.randint(10, 1000), "units": random.randint(1, 100)}

def list_collections():
    collection_names = db.list_collection_names()
    return collection_names

def get_all_documents(collection):
    documents_list = []
    for document in collection.find():
        documents_list.append(document)
    return documents_list

def get_document(collection, _id):
    document = collection.find_one({'_id': ObjectId(_id)})
    return document

def save_document(collection, document):
    _id = collection.insert_one(document).inserted_id
    return _id

# Show all collections
pprint(list_collections())
# Get all documents
pprint(get_all_documents(products_collection))
# get document by '_id'
pprint(get_document(products_collection, '6436e020a2403e9158aee52c'))
# Save document (product)
print('Saved document with _id : ', save_document(products_collection, test_product))