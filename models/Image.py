from models.Config import Config
import datetime


class Image:
    def __init__(self, config: Config, path):
        self.config = config
        self.path = path
        self.device_id = config.device_id
        self.sensor_id = config.device_id
        self.type= "image"
        self.date = datetime.datetime.now()
        self.filename = "image_" + self.device_id + "_" + self.sensor_id + str(self.date)


    def upload_image(self, path):
        image_blob = self.config.bucket.blob(self.filename)
        image_blob.upload_from_filename(path)