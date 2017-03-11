
class JsonDataWrapper:
    '''
    Reference: http://stackoverflow.com/questions/38464302/wrapping-a-python-class-around-json-data-which-is-better

    '''

    def __init__(self, json_data):
        '''
        Interface between API reference and underlying implementation through json.

        :param json_data: The json representation of the object as provided by the API.
        '''
        self._data = json_data

    def get(self, name):
        '''

        :param name: Key to search for in self.json_data
        :return: Value corresponding to key 'name' in self.json_data
        '''
        return self._data[name]


class Pin(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/pins/?
    '''

    def __init__(self, json_data):
        super().__init__(json_data)
        # TODO: Confirm timezone of Pin._created_at.
        # TODO: Create class container for Pin._attribution. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the Pin on Pinterest.
        :param _link: Hyperlink to the pin.
        :param _url: The URL of the Pin on Pinterest.
        :param _creator: Pinterest user that created the pin. models.PinterestUser
        :param _board: Pinterest board the Pin is on. models.Board
        :param _created_at: The date the Pin was created. ISO 8601.
        :param _note: The user-entered description of the Pin.
        :param _color: The dominant color of the Pin’s image in hex code format.
        :param _repin_count: Number of repins this Pin has. NOT constant.
        :param _comment_count: Number of comments this Pin has. NOT constant.
        :param _like_count: Number of likes this Pin has. NOT constant.
        :param _attribution: The source data for videos, including the title, URL, provider, author name, author URL and provider name.

        '''
        self._id = None
        self._link = None
        self._url = None
        self._creator = None
        self._board = None
        self._created_at = None
        self._note = None
        self._color = None
        self._counts = None
        self._media = None
        self._attribution = None
        self._image = None
        self._metadata = None
        self._repin_count = None
        self._comment_count = None
        self._like_count = None

    @property
    def id(self): return self.get('id')

    @property
    def link(self): return self.get('link')

    @property
    def url(self): return self.get('url')

    @property
    def creator(self): return self.get('creator')

    @property
    def board(self): return self.get('board')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def original_link(self): return self.get('original_link')

    @property
    def note(self): return self.get('note')

    @property
    def color(self): return self.get('color')

    @property
    def link(self): return self.get('link')

    @property
    def board(self): return self.get('board')

    @property
    def image(self): return self.get('image')

    @property
    def repin_count(self): return self.get('counts').get('repins')

    @property
    def comment_count(self): return self.get('counts').get('comments')

    @property
    def like_count(self): return self.get('counts').get('likes')

    @property
    def metadata(self): return self.get('metadata')


class Board(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/boards/
    '''

    def __init__(self, json_data):
        super().__init__(json_data)
        # TODO: Confirm timezone of Board._created_at.
        # TODO: Create class container for Board._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the board on Pinterest.
        :param _name: The name of the board.
        :param _url: The link to the board.
        :param _description: The user-entered description of the board.
        :param _creator: The creator of the board. pypin.models.User.
        :param _created_at: The date the board was created. ISO 8601 format.
        :param _pin_count: Number of pins on the board. NOT constant.
        :param _collaborator_count: Number of collaborators on the board. NOT constant.
        :param _follower_count: Number of followers this board has. NOT constant.
        :param _image: The board’s profile image. The response returns the image’s URL, width and height.

        '''
        self._counts = None
        self._created_at = None
        self._description = None
        self._id = None
        self._image = None
        self._name = None
        self._url = None
        self._creator = None

    @property
    def pin_count(self): return self.get('counts').get('pins')

    @property
    def collaborator_count(self): return self.get('counts').get('collaborators')

    @property
    def follower_count(self): return self.get('counts').get('followers')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def description(self): return self.get('description')

    @property
    def id(self): return self.get('id')

    @property
    def image(self): return self.get('image')

    @property
    def name(self): return self.get('name')

    @property
    def url(self): return self.get('url')

    @property
    def creator(self): return self.get('creator')


class User(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/users/
    '''

    def __init__(self, json_data):
        super().__init__(json_data)
        # TODO: Confirm timezone of User._created_at.
        # TODO: Create class container for User._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the user on Pinterest.
        :param _username: The user’s Pinterest username.
        :param _first_name: The user’s first name.
        :param _last_name: The user’s last name.
        :param _bio: The text in the user’s “About you” section in their profile.
        :param _created_at: The date the user created their account. ISO 8601 format.
        :param _pin_count: Number of pins the user has posted and are available. NOT constant.
        :param _follower_count: Number of followers this user has. NOT constant.
        :param _following_count: Number of accounts this user is following. NOT constant.
        :param _board_count: Number of boards this user has. NOT constant.
        :param _like_count: Number of likes this user has. NOT constant.
        :param _image: The user’s profile image. The response returns the image’s URL, width and height.
        '''
        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._bio = None
        self._created_at = None
        self._pin_count = None
        self._follower_count = None
        self._board_count = None
        self._like_count = None
        self._image = None

    @property
    def id(self): return self.get('id')

    @property
    def username(self): return self.get('username')

    @property
    def first_name(self): return self.get('first_name')

    @property
    def last_name(self): return self.get('last_name')

    @property
    def bio(self): return self.get('bio')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def pin_count(self): return self.get('counts').get('pins')

    @property
    def following_count(self): return self.get('counts').get('following')

    @property
    def follower_count(self): return self.get('counts').get('followers')

    @property
    def board_count(self): return self.get('counts').get('boards')

    @property
    def like_count(self): return self.get('counts').get('likes')

    @property
    def image(self): return self.get('image')

