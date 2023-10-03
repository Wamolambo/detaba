from pymongo import MongoClient
conn = MongoClient('mongodb+srv://mangodb:mangodb@cluster0.pxkjnl6.mongodb.net/?retryWrites=true&w=majority')
db = conn['cnn_db']
collection = db['cnn_collection']

