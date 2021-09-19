import glob
import os
import pyrebase
import json

config = json.load(open('config.json'))


path = "uploads/*jpg"
files = sorted(glob.iglob(path), key=os.path.getctime,reverse=True)

recent = files[0]

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

storage.child(recent.replace("uploads\\", "")).put(recent)