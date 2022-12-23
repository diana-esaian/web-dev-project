from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://diana_esaian:lolps@moscow.n0szos7.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('moscow')
user_collection = pymongo.collection.Collection(db, 'locations')

data_db = []

tbl="<tr><td>Топоним</td><td>Частотность</td><td>Век</td></tr>"
data_db.append(tbl)

for y in mycol.find():
    a = "<tr><td>%s</td>"%y['топоним']
    stud.append(a)
    b = "<td>%s</td>"%y['частотность']
    stud.append(b)
    c = "<td>%s</td></tr>"%y['век']
    stud.append(c)
