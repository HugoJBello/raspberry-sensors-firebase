from models.Config import Config
from models.Image import Image
from picamera import PiCamera
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
import time

class Camera:
    def __init__(self, config: Config):
        self.config = config

    def shot(self, camera):
        path = '../image.jpg'
        camera.capture(path)
        #camera.stop_preview()

        image = Image(config=self.config, path=path)
        image.upload_image()
        sleep(5)


    def shot_periodically(self):
        print("taking camera shot")
        camera = PiCamera()
        sched = BackgroundScheduler()

        sched.add_job(lambda: self.shot(camera), 'interval', seconds=5)
        sched.start()

        try:
            # This is here to simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(5)
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            sched.shutdown()
            print("eding process")




        pass
