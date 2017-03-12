import json
import requests
import urllib.request

class API(object):
    """Pinterest API"""

    TIMEOUT = 20

    def __init__(self, access_token=None,
                 host='https://api.pinterest.com', api_root='/v1',
                 wait_on_rate_limit=False, wait_on_rate_limit_notify=False):
        """ Api instance Constructor

        :param auth_handler:
        :param host:  url of the server of the rest api, default:'api.twitter.com'
        :param api_root: suffix of the api version, default:'/1.1'
        :param wait_on_rate_limit: If the api wait when it hits the rate limit, default:False
        :param wait_on_rate_limit_notify: If the api print a notification when the rate limit is hit, default:False
        """
        self.access_token = access_token
        self.api_root = api_root
        self.host = host
        self.wait_on_rate_limit = wait_on_rate_limit
        self.wait_on_rate_limit_notify = wait_on_rate_limit_notify


    @staticmethod
    def call(url, method='get', params=None):
        """
        API call to Pinterest
            url: String, API endpoint with access token attached
            method:  String, HTTP method, get post put delete
            params: Dict, optional, supply necessary parameters
            fields: String, optional, expected return fields,
                will return default fields if not specified
        """
        result = getattr(requests, method)(url, timeout=API.TIMEOUT, data=params)
        # print (request.json())
        if result.status_code in [200, 201]:
            return result.json()
        elif result.status_code == 404:
            raise pypin.exceptions.PyPinContentNotFoundError(response=result)
        else:
            raise pypin.exceptions.PyPinUnhandledResponseCodeError(response=result)

    def get_me(self):
        """Get the authenticated user's Pinterest account info"""
        api_endpoint = self.host + self.api_root +'/me/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_likes(self):
        """Get the pins that the authenticated user likes"""
        api_endpoint = self.host + self.api_root +'/me/likes/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_followers(self):
        """Get the authenticated user's followers"""
        api_endpoint = self.host + self.api_root +'/me/followers/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_following_boards(self):
        """Get the boards that the authenticated user follows"""
        api_endpoint = self.host + self.api_root +'/me/following/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_following_users(self):
        """Get the Pinterest users that the authenticated user follows"""
        api_endpoint = self.host + self.api_root +'/me/following/users/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_following_interests(self):
        """Get the interests that the authenticated user follows"""
        api_endpoint = self.host + self.api_root +'/me/following/interests/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def follow_user(self, user_name):
        """Follow a user
		parameters:
             name: 'user_name',
             description: 'user name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/users/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', { 'user': user_name })


    def unfollow_user(self, user_name):
        """Unfollow a user
		parameters:
             name: 'user_name',
             description: 'user name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/users/' + user_name
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'delete')

    def follow_board(self, board_id):
        """Follow a board
		parameters:
             name: 'board_id',
             description: 'board name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', { 'board': board_id })

    def unfollow_board(self, board_id):
        """Unfollow a board
		parameters:
             name: 'board_id',
             description: 'board name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/boards/' + board_id
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'delete')

    def get_my_pins(self):
        """Get all of authenticated users's pins"""
        api_endpoint = self.host + self.api_root +'/me/pins/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_boards(self):
        """Get all of authenticated users's boards"""
        api_endpoint = self.host + self.api_root +'/me/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'get')

    def get_user(self, username):
        """Get the account info for a Pinterest user"""
        pass

    def create_board(self, board_info):
        """Create a new board
        parameters:
             name: 'board name',
             description: 'Board description, optional'
        """
        api_endpoint = self.host + self.api_root +'/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', board_info)

    def create_pin(self, pin_info):
        """Create a pin on a board
        pinInfo structure:
             board: '<username>/<board_name>' OR '<board_id>',
             note: 'My note'
             link: 'https://www.google.com',
             image_url: 'http://marketingland.com/pinterest-logo-white-1920.png'
        """
        api_endpoint = self.host + self.api_root +'/pins/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', pin_info)

    def get_public_pin(self, pin_id, desired_attributes=None):
        """GET - Gets data on a pin using the /v1/pins/<pin>/ endpoint
        available attributes:
            ['id', 'link', 'note', 'url', 'color', 'attribution', 'board',
                'counts', 'created_at', 'creator', 'original_link', 'media', 'image', 'metadata']


            Parameters
            ----------
            pin_id : string
                The id of the pin to retrieve.
            desired_attributes : list[string], optional
                The list of attributes to request for the associated pin.

            Returns
            -------
            json_array
                The response from Pinterest.

            Raises
            -------
            RuntimeError
                If the response code != 200, this exception will be raised along
                with the return code of the request.

        """
        api_endpoint = self.host + self.api_root + "/pins/{:s}".format(pin_id)
        request_url = api_endpoint + '?access_token=' + self.access_token
        if desired_attributes:
            desired_attributes = [atr + '%2C' for atr in desired_attributes]
            request_url += "&fields={}".format(''.join(desired_attributes))
            request_url = request_url.rstrip('%2C')
            # print(request_url)
        return API.call(request_url)
