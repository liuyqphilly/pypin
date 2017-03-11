
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
        print(json_data)
        # TODO: Confirm timezone of Pin._created_at.
        # TODO: Create class container for PinterestPin._attribution. Currently <dict>.
        '''

        :param json_data: The

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
    def counts(self): return self.get('counts')

    @property
    def metadata(self): return self.get('metadata')


