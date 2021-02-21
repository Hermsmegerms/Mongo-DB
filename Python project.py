import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']

def insert_document(document):
  try:
  result=collection.save(document)
  except ValidationError as ve:
  abort(400, str(ve))
  return result

def main():
  myDocument = { "keyName" : "test value data"}
  print insert_document(myDocument)

main()