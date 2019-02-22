class ActionError(Exception):
    pass


class InvalidCredentials(ActionError):
    """ Exception raised at login when credentials are invalid """
    def __init__(self, msg=None):
        if msg is None:
            msg = "Invalid Credentials"
        super(InvalidCredentials, self).__init__(msg)


class NotFoundError(ActionError):
    """ Exception raised when the selected choice is unavailable """

    def __init__(self, option, resource, message=None):
        self.option = option
        self.resource = resource
        if message is None:
            message = '{} not found in {}'.format(option, resource)
        super(NotFoundError, self).__init__(option, resource, message)
