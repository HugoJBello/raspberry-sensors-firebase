import unittest
from models.Config import Config
from models.Image import Image
from dotenv import load_dotenv
load_dotenv()

class TestConfig(unittest.TestCase):

    def test_load_image(self):
        config = Config()
        image = Image(config,"Config.py")
        image.upload_image()
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()