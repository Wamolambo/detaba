###############################################################################################
#  title="CCN API",
#  description="This API performs the CRUD methods[GET,DELETE,POST,UPDATE] for the CCN News Feed",
#  version="2.5.0",
# author="Wamolambo Lucky Ramasila"
##############################################################################################
from fastapi import APIRouter
from config.db import collection
from schemas.schema import serializeList, userEntity,serializeDict,usersEntity
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
    article = serializeList(collection.find())
    return {"status": "Ok","data": article}

# Find one record by ID
@article.get('/{Find_one_record_by_ID}/')
async def find_one_records(id: str):
    article = collection.find_one({"_id":ObjectId(id)})
    return userEntity(article)

# Create new record
@article.post('/{Create_new_record}')
async def create_one_record(article: Article):
    _id = collection.insert_one(dict(article))
    article = serializeList(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": article}


# Update existing record
@article.put('/{Update_existing_record}')
async def update_one_record(id,article: Article):
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(article)})
    return userEntity(collection.find_one({"_id":ObjectId(id)}))

# Delete one record by ID
@article.delete('/{Delete_one_record_by_ID}')
async def delete_one_record(id,article: Article):
    return userEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))
