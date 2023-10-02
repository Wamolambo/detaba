###############################################################################################
#  title="CCN API",
#  description="This API performs the CRUD methods[GET,DELETE,POST,UPDATE] for the CCN News Feed",
#  version="2.5.0",
# author="Wamolambo Lucky Ramasila"
##############################################################################################
from fastapi import APIRouter
from config.db import conn
from schemas.schema import serializeList, userEntity,serializeDict,test
from bson import ObjectId
from models.model import Article

import requests
from bson import ObjectId
from json import JSONDecodeError
from fastapi import FastAPI, Request

article = APIRouter() 

# Find all records
@article.get('/{Find_all_records}')
async def find_all_records():
    db = conn['cnn_db']
    collection = db['cnn_collection']
    data = collection.find()
    return serializeList(data)

# Find one record by ID
@article.get('/{Find_one_record_by_ID}')
async def find_one_records(id):
    db = conn['cnn_db']
    collection = db['cnn_collection']
    return userEntity(collection.find_one({"_id":ObjectId(id)}))

# Create new record
@article.post('/{Create_new_record}')
async def create_one_record(article: Article):
    db = conn['cnn_db']
    collection = db['cnn_collection']
    collection.insert_one(dict(article))
    return serializeList(collection.find())

# Update existing record
@article.put('/{Update_existing_record}')
async def update_one_record(id,article: Article):
    db = conn['cnn_db']
    collection = db['cnn_collection']
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(article)})
    return userEntity(collection.find_one({"_id":ObjectId(id)}))

# Delete one record by ID
@article.delete('/{Delete_one_record_by_ID}')
async def delete_one_record(id,article: Article):
    db = conn['cnn_db']
    collection = db['cnn_collection']
    return userEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))
