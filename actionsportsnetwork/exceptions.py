class ActionError(Exception):
    pass


class InvalidCredentials(ActionError):
    def __init__(self, msg=None):
        if msg is None:
            msg = "Invalid Credentials"
        super(InvalidCredentials, self).__init__(msg)


class NotFoundError(ActionError):
    pass
