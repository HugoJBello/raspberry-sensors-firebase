from dotenv import load_dotenv
from sensors.Camera import Camera
from models.Config import Config
from apscheduler.schedulers.background import BackgroundScheduler

import os

def run_sensors():
    config = Config()
    camera = Camera(config)
    camera.shot()

def main():

    print("starting process")
    sched = BackgroundScheduler()
    sched.daemonic = False
    sched.start()
    sched.add_job(run_sensors, 'interval', seconds=10)
    print("eding process")

if __name__ == '__main__':
	main()