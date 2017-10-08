import json


def load_projects():
    return json.load(open('data/project.json'))


def load_forecast_data(pid):
    return json.load(open(get_forecast_data_path(pid)))


def get_forecast_data_path(pid):
    return 'data/forecast/%s.json' % pid
