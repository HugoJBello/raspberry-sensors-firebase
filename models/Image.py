from models.Config import Config


class Image:
    def __init__(self, config: Config):
        self.config = config

    def upload_image(self, path):
        image_blob = self.config.bucket.blob(path)
        image_blob.upload_from_filename(path)