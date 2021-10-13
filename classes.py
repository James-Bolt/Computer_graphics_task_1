
import json

class University(object):
    def __init__(self, input_data):
        with open("input_university.json", "r") as read_file:
            data = json.load(read_file)
            self.a = data['value']

