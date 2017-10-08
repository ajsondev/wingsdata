import json


def load_projects():
    return json.load(open('data/projects.json'))
