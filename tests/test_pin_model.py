import pypin
import unittest
import os

class TestPinModel(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'])
        self.pin = self.api.get_public_pin('132645151506393653')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertTrue(isinstance(self.pin, pypin.Pin), msg='Pin should be type pypin.models.Pin')

    def test_id_getter(self):
        self.assertIsNotNone(self.pin.id, msg='Pin id should be initialized.')

if __name__ == '__main__':
    unittest.main()