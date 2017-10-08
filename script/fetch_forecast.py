import json
from urllib.request import urlopen
import logging

from util import load_projects
from project.database import db


def fetch_forecast(addr):
    db.forecast.remove({'project_addr': addr})
    offset = 0
    while True:
        print('Processing page #%d' % (offset // 10))
        url = (
            'https://api-experimental.wings.ai/api/%s'
            '/forecasting/forecasts?limit=10&offset=%d'
            % (addr, offset)
        )
        res = None
        for x in range(3):
            try:
                res = json.loads(urlopen(url).read().decode('utf-8'))
            except OSError as ex:
                logging.error(ex)
        if not res:
            raise Exception('Could not download URL: %s' % url)
        if not res['data']:
            break
        for item in res['data']:
            cast = {
                'raw': item,
                'project_addr': addr,
            }
            db.forecast.save(cast)
        offset += 10


def main(**kwargs):
    projects = load_projects()
    for proj in projects:
        print('Processing project %s' % proj['name'])
        fetch_forecast(proj['address'])
