class PyPinException(Exception):
    def __init__(self, response):
        self.response = response

class PyPinContentNotFoundError(PyPinException):

    def __str__(self):
        return '404 response from Pinterest. Content not found.'

class PyPinUnhandledResponseCodeError(Exception):

    def __str__(self):
        return 'Unhandled response code returned from Pinterest.'
