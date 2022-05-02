#!/usr/bin/env python3
import requests
"""
Comments module
"""


class User:
    """ Class definition """
    urls = {
        'url_login': 'https://intranet.hbtn.io/auth/sign_in',
        'url_google': 'https://www.google.com',
        'url_proyects': 'https://intranet.hbtn.io/projects/current'
    }

    def __init__(self, email, pwd):
        """ Function definition """
        self.email = email
        self.password = pwd
        self.session = requests.Session()

    def credentails(self):
        """ Function definition """
        crts = {
            'email': self.email,
            'password': self.password
        }
        return crts

    def play_load_login(self):
        """ Function definition """
        from bs4 import BeautifulSoup
        content_page = self.session.get(self.urls['url_login'])
        html = BeautifulSoup(content_page.text, "html.parser")
        ruler_css = 'form > input[name="authenticity_token"]'
        token = html.select(ruler_css)[0].get('value')
        play_load = {
            'user[login]': self.email,
            'user[password]': self.password,
            'authenticity_token': token,
            'commit': 'submit'
        }
        return play_load
