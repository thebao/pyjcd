class PYJCDException(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{0}'.format(self.message)


class APICallError(PYJCDException):
    pass

class ParseError(PYJCDException):
    pass