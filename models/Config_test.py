import unittest
from models.Config import Config
from dotenv import load_dotenv
load_dotenv()

class TestConfig(unittest.TestCase):

    def test_load_config(self):
        config = Config()
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()