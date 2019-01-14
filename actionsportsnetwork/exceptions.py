class ActionError(Exception):
    pass

class InvalidCredentials(ActionError):

    pass

class NotFoundError(ActionError):
    pass
