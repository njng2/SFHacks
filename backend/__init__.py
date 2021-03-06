from flask import *
import pymongo
app = Flask(__name__)
import json
import bson.json_util
import mongoengine as mg


class Assignments(mg.EmbeddedDocument):
    duedate = mg.DateField()
    title = mg.StringField()
    body = mg.StringField()

class User(mg.Document):
    uid = mg.StringField(required=True)
    assignments = mg.ListField(mg.EmbeddedDocumentField(Assignments))

@app.route("/mood")
def readdb():
    pass
    # db.test_collection.insert_one({"name": "moody"})
    # return bson.json_util.dumps(list(db.test_collection.find({})))

@app.route("/newassignment", methods=["POST"])
def newassignment():
    data = request.get_json()
    uid = data["uid"]
    duedata = data["duedate"]
    title = data["title"]
    body = data["body"]
    
    

    return "A"

@app.route("/echo", methods=["POST"])
def echo():
    return request.get_json()

if __name__ == '__main__':
    app.run(debug=True)