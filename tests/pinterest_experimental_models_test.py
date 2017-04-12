import pypin
import unittest
import os

'''
These tests are meant for the models of the api/v3 endpoints. They are in no way the same as the api/v1 responses.
'''

class TestBoardPinsV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.board_pins = self.api.get_public_board_pins_v3('107734684775018526')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.board_pins, pypin.BoardPinsV3, msg='BoardPins should be type pypin.models.BoardPinsV3')

    def test_board_pins_id_getter(self):
        self.assertIsNotNone(self.board_pins.id, msg='BoardPins id should be initialized.')

    def test_board_pins_iter(self):
        c = 0
        for pin in self.board_pins:
            c += 1
        self.assertEqual(c, self.api.get_public_board(self.board_pins.id).pin_count,
                         msg='Iter should loop over the number of pins on the board.')

class TestPinsV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.pin = self.api.get_public_pin_v3('442830575846619266')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.pin, pypin.PinV3, msg='pin should be type pypin.models.PinV3')

    def test_board_pins_id_getter(self):
        self.assertIsNotNone(self.pin.id, msg='pin id should be initialized.')

class TestUserFollowersV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.followers = self.api.get_user_followers_v3('hawkins6654')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.followers, pypin.UserFollowersV3, msg='pin should be type pypin.models.UserFollowersV3')

    def test_status(self):
        self.assertEqual(self.followers.get('status'), "success", msg='status should be "success".')

    def test_paginated(self):
        for follower in self.followers:
            pass
            # print(follower)

class TestUserFollowingV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.following = self.api.get_user_following_v3('hawkins6654')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.following, pypin.UserFollowingV3, msg='pin should be type pypin.models.UserFollowersV3')

    def test_status(self):
        self.assertEqual(self.following.get('status'), "success", msg='status should be "success".')

    def test_paginated(self):
        for user in self.following:
            pass
            # print(follower)

if __name__ == '__main__':
    unittest.main()