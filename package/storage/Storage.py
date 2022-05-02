#!/usr/bin/env python3
""" Comment module """
import json


class Storage:
    """ Class definition """
    def save(self, data):
        """ Function definition """
        with open("config.json", "w") as file:
            json.dump(data, file)

    def load(self):
        """ Function definition """
        try:
            with open("config.json", "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            pass

    def show(self):
        """ Function definition """
        with open("config.json", "r") as file:
            data = json.load(file)
            print(data)

    def delete(self):
        """ Function definition """
        self.save({})
