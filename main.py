from dotenv import load_dotenv
from sensors.Camera import Camera
from models.Config import Config
from apscheduler.schedulers.background import BackgroundScheduler
import time
from dotenv import load_dotenv
load_dotenv()



def run_sensors():
    config = Config()

    print("running sensors")
    camera = Camera(config)
    sched = BackgroundScheduler()
    sched.add_job(camera.shot, 'interval', seconds=10)
    sched.start()
    return sched

def main():

    print("starting process")
    sched = run_sensors()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()
        print("eding process")


if __name__ == '__main__':
	main()