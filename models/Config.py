import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

class Config:
    def __init__(self):
        self.sensor_id = None
        self.device_id = None
        self.db = None

        self.initialize_firebase()
        self.load_from_env()


    def initialize_firebase(self):
        with open("firebase_config_json_token.json", "w") as text_file:
            text_file.write(os.getenv("firebase_config_json_token"))

        cred = credentials.Certificate("firebase_config_json_token.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        self.bucket = storage.bucket("house-monitor-pi.appspot.com")

        #imagePath = "Config.py"
        #imageBlob = self.bucket.blob(imagePath)
        #imageBlob.upload_from_filename(imagePath)

    def load_from_env(self):
        self.sensor_id = os.getenv("sensor_id")
        self.device_id = os.getenv("device_id")

