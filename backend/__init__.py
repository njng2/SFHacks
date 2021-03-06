from flask import *
import pymongo
app = Flask(__name__)
import json
import bson.json_util
import mongo

client = pymongo.MongoClient("")
db = client.data


@app.route("/mood")
def readdb():
    db.test_collection.insert_one({"name": "moody"})
    return bson.json_util.dumps(list(db.test_collection.find({})))


if __name__ == '__main__':
    app.run(debug=True)