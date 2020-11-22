import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
import datetime

class Config:
    def __init__(self):
        self.sensor_id = None
        self.device_id = None
        self.interval_for_images = 60*5
        self.db = None

        self.initialize_firebase()
        self.load_from_env()
        self.update_config()


    def initialize_firebase(self):
        with open("firebase_config_json_token.json", "w") as text_file:
            text_file.write(os.getenv("firebase_config_json_token"))

        cred = credentials.Certificate("firebase_config_json_token.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        self.bucket = storage.bucket("house-monitor-pi.appspot.com")


    def load_from_env(self):
        self.sensor_id = os.getenv("sensor_id")
        self.device_id = os.getenv("device_id")
        self.interval_for_images = int(os.getenv("interval_for_images"))
        print(self.sensor_id, self.device_id, self.interval_for_images)
        if  (self.interval_for_images == None or self.interval_for_images == ""):
            self.interval_for_images = 60*5


    def update_config(self):
        data = {
            "device_id": self.device_id,
            "sensor_id": self.sensor_id,
            "interval_for_images": self.interval_for_images,
            "date": datetime.datetime.now()
        }
        print("updating config: " + self.device_id)
        # Add a new doc in collection 'cities' with ID 'LA'
        self.db.collection(u'devices').document(self.device_id).set(data)

