from dotenv import load_dotenv
from sensors.Camera import Camera
from models.Config import Config
import time
from dotenv import load_dotenv
load_dotenv()



def run_sensors():
    config = Config()

    print("running sensors")
    camera = Camera(config)
    camera.shot_periodically()

def main():

    print("starting process")
    run_sensors()




if __name__ == '__main__':
	main()