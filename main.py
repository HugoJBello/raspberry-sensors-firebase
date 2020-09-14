from dotenv import load_dotenv
from sensors.Camera import Camera
from models.Config import Config
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os

def run_sensors():
    config = Config()
    camera = Camera(config)
    camera.shot()

def main():

    print("starting process")
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(run_sensors, 'interval', seconds=10)
    print("eding process")

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()

if __name__ == '__main__':
	main()