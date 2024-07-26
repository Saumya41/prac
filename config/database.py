from pymongo import MongoClient

client= MongoClient("mongodb+srv://admin:Test1234@cluster0.mfnioyb.mongodb.net/?appName=Cluster0")

db= client.assessment

collection_name= db["question"]
