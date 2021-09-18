import firebase_admin
from firebase_admin import credentials, db
import json


class dataBase():
    def __init__(self):
        cred = credentials.Certificate("./rebug-aecaa-firebase-adminsdk-wg3tm-fa43c244bc.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL':"https://rebug-aecaa-default-rtdb.firebaseio.com/"
            })

        self.ref = db.reference("/events")
    
    def add(self, location, volunteers, date):
        someEvent = {
            "Location": location,
            "People needed": volunteers,
            "Time of clean up": date
        }
        self.ref.push(someEvent)

    def get(self):
        data = self.ref.get()
        with open('template.json', 'w') as f:
            json.dump(data, f)
        return data,list(data.keys())

db = dataBase()
print(db.get())