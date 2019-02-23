"""This is the basic session module"""

import base64
import requests


class ActionSession(requests.Session):
    """Session object"""

    def __init__(self, *args, **kwargs):
        super(ActionSession, self).__init__(*args, **kwargs)

        self.headers.update(
            {'User-Agent': 'Action-AppStore/13471 CFNetwork/894 Darwin/17.4.0'})

    def init_auth_credentials(self, username, password):
        """
        :param username:
        :param password:
        :return:
        """
        credentials = base64.b64encode('{}:{}'.format(username, password).encode())
        self.headers.update({'Authorization': 'Basic {}'.format(credentials.decode())})

