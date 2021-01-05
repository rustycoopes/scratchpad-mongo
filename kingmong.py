import pprint
import pymongo

def loaddata():
    # TODO : connects to mongo and loads some data
    # console out some strucute.

    client = pymongo.MongoClient('mongodb+srv://russ-admin:cooperman@cluster0.gqxah.mongodb.net/sample_weatherdata?retryWrites=true&w=majority')
    db = client.test_database
    posts = collection = db.data
    pprint(posts.find_one())

    
    return None


def savedata():
    # TODO : connects to mongo and saves a json document - somethign based on time
    # with an index.
    return None