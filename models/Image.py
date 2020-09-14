from models.Config import Config
import datetime
import os


class Image:
    def __init__(self, config: Config, path):
        self.config = config
        self.path = path
        self.device_id = config.device_id
        self.sensor_id = config.device_id
        self.type = "image"
        filename, file_extension = os.path.splitext(path)
        self.extension = file_extension

        self.date = datetime.datetime.now()
        self.filename = "image_" + self.device_id + "_" + self.sensor_id + "_" + str(self.date) + self.extension

    def upload_image(self):
        image_blob = self.config.bucket.blob(self.filename)
        image_blob.upload_from_filename(self.path)
        data = {
            "device_id": self.device_id,
            "sensor_id": self.sensor_id,
            "type": self.type,
            "date": self.date,
            "filename": self.filename,
            "extension": self.extension
        }
        print("uploading image: " + self.filename)
        # Add a new doc in collection 'cities' with ID 'LA'
        self.config.db.collection(u'images').document(self.filename).set(data)
