from models.Config import Config
from models.Image import Image
from picamera import PiCamera
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
import time

class Camera:
    def __init__(self, config: Config):
        self.config = config
        self.interval = self.config.interval_for_images

    def shot(self, camera):
        print("taking shot")
        path = '../image.jpg'
        camera.capture(path, use_video_port=True)

        image = Image(config=self.config, path=path)
        image.upload_image()


    def shot_periodically(self):
        print("running job camera shot")
        camera = PiCamera()
        sched = BackgroundScheduler()

        print("adding job each " + str(self.interval))
        if self.interval == None:
            self.interval = 200
        sched.add_job(lambda: self.shot(camera), 'interval', seconds=self.interval)
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
