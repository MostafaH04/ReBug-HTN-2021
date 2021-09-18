import glob
import os
import pyrebase

path = "uploads/*jpg"
files = sorted(glob.iglob(path), key=os.path.getctime,reverse=True)

recent = files[0]

config = {
  'apiKey': "AIzaSyC1DIqvIw_BEdLhWzdlF301BWWmbuNhyhA",
  'authDomain': "rebug-aecaa.firebaseapp.com",
  'databaseURL': "https://rebug-aecaa-default-rtdb.firebaseio.com",
  'projectId': "rebug-aecaa",
  'storageBucket': "rebug-aecaa.appspot.com",
  'serviceAccount': "serviceAccountKey.json"
};

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

storage.child(recent).put(recent)