from models.Config import Config
from models.Image import Image
from picamera import PiCamera
from time import sleep


class Camera:
    def __init__(self, config: Config):
        self.config = config

    def shot(self):
        print("taking camera shot")
        camera = PiCamera()
        camera.start_preview()
        sleep(5)

        path = '../image.jpg'
        camera.capture(path)
        camera.stop_preview()

        image = Image(config=self.config, path=path)
        image.upload_image()

        pass
