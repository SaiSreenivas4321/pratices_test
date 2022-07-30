import pymongo
# client = pymongo.MongoClient("mongodb+srv://saisreenivas:Sreenu@@123456789@atlascluster.y6mad.mongodb.net/?retryWrites=true&w=majority")
# db = client.

client = pymongo.MongoClient("mongodb+srv://saisreenivas:sreenu123456789@atlascluster.y6mad.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# d ={
#     "name":"saisreenivas",
#     "email":"sreenivas@ineuron.ai",
#     "surname":"BalasaKarunakar"
#
# }
#
# db1 = client['monogotest']
# collecction =db1['test']
# collecction.insert_one(d)


data ={
    "name": "Sai Sreenivas",
    "Email_id": "Sai.ineuron@ai",
    "Subject":"Data Science all Fields"
}

listofrecords=[{
    "companyname":"google",
    "product":"pg in data science",
    "courseroffered":"data science related",
},

{
    "companyname":"TCS",
    "product":"Advanced in data science",
    "courseroffered":"data science related",
},

{
    "companyname":"google",
    "product":"pg in data science",
    "courseroffered":"data science related",
}

]

database = client['myInfo']
collection = database["sai"]
collection.insert_one(data)
collection.insert_many(listofrecords)

lisofrecords=collection.find()

for i in lisofrecords:
    print(i)
# if (i == 'companyname'):
#     print(i)

data = collection.find({"companyname":"google"})
for i in data:
    print(i)