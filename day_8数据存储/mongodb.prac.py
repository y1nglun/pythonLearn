import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

std1 = {
    'id': 20170101,
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
std2 = {
    'id': 20170102,
    'name': 'Mike',
    'age': 22,
    'gender': 'male'
}

result = collection.insert_many([std1, std2])
print(result)
