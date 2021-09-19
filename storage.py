import glob
import os
import pyrebase
import json

path = "uploads/*jpg"
files = sorted(glob.iglob(path), key=os.path.getctime,reverse=True)

if files:
  recent = files[0]

config = {
    "apiKey": "AIzaSyC1DIqvIw_BEdLhWzdlF301BWWmbuNhyhA",
    "authDomain": "rebug-aecaa.firebaseapp.com",
    "databaseURL": "https://rebug-aecaa-default-rtdb.firebaseio.com/",
    "projectId": "rebug-aecaa",
    "storageBucket": "rebug-aecaa.appspot.com",
    "serviceAccount": "serviceAccountKey.json",
    "messagingSenderId": "1057776412856"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def upload(location) -> None:
  storage.child(f"uploads/{location}/0.jpg").put(recent)
  os.remove(recent)
  

def download(location) -> None:
  storage.child(f"uploads/{location}/images.jpg").download(path="localImages/0.jpg", filename="0.jpg")

