import glob
import os
import pyrebase
import json

path = "uploads/*jpg"
files = sorted(glob.iglob(path), key=os.path.getctime,reverse=True)

if files:
  recent = files[0]

config = json.load(open('config.json'))

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def upload(location) -> None:
  storage.child(recent).put(recent)
  

def download(location) -> None:
  storage.child(f"uploads/{location}/images.jpg").download(path="localImages/0.jpg", filename="0.jpg")

