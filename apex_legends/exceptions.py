class UnauthorizedError(Exception):

    def __init__(self, message='API key invalid or missing'):
        super().__init__(message)


class NotFoundError(BaseException):

    def __init__(self, message='The specified resource was not found'):
        super().__init__()


class UnknownPlayerError(BaseException):

    def __init__(self, message='The specified player was not found'):
        super().__init__()


class ServerError(BaseException):

    def __init__(self, message='There is an error with the server.'):
        super().__init__()
