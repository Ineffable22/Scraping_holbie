#!/usr/bin/env python3
"""
This module helps to create persistent sessions between diferent
executions of the program. A file is used as a cache to store information
about sessions.

Classes
-------
    My_Sessions
"""
import pickle
import os
from urllib.parse import urlparse
import requests


class My_Session:
    """
    Class definition to instantiate session objects. That allow interaction
    with web pages through different types of requests.
    """
    index_file = "_session_file"
    urls = {
        'sign_in': 'https://intranet.hbtn.io/auth/sign_in'
    }

    def __init__(self,
                 url_dest='https://intranet.hbtn.io/auth/sign_in',
                 play_load=None,
                 force_login=False
                 ):
        url_data = urlparse(url_dest)
        self.url_dest = url_dest
        self.play_load = play_load
        self.file_session = url_data.netloc + My_Session.index_file

        self.login(force_login)

    def login(self, force_login=False):
        read_file_session = False

        if os.path.exists(self.file_session) and not force_login:
            with open(self.file_session, 'rb') as file:
                self.session = pickle.load(file)

        if not read_file_session:
            self.session = requests.Session()
            res = self.session.post(self.url_dest, data=self.play_load)
            print(res)
            self.save_session()

    def save_session(self):
        with open(self.file_session, 'wb') as file:
            pickle.dump(self.session, file)
