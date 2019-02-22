import requests
import os
from actionsportsnetwork.exceptions import *


class BaseClient(object):

    def __init__(self, username=None, password=None):
        """

        :param username:
        :param password:
        """
        self.username = username
        self.password = password
        self.url = ''