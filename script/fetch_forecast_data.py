import json
from urllib.request import urlopen
import logging

from util import load_projects, get_forecast_data_path


def fetch_forecast(project_id, project_addr):
    offset = 0
    forecast_list = []
    while True:
        print('Processing page #%d' % (offset // 10))
        url = (
            'https://api-experimental.wings.ai/api/%s'
            '/forecasting/forecasts?limit=10&offset=%d'
            % (project_addr, offset)
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
            forecast_list.append(item)
        offset += 10
    with open(get_forecast_data_path(project_id), 'w') as out:
        out.write(json.dumps(forecast_list))


def setup_arg_parser(parser):
    parser.add_argument('pid')


def main(pid, **kwargs):
    projects = load_projects()
    if pid == 'all':
        pids = [x['id'] for x in projects]
    else:
        pids = pid.split(',')
    for pid in pids:
        proj = [x for x in projects if x['id'] == pid][0]
        print('Processing project %s' % proj['name'])
        fetch_forecast(proj['id'], proj['address'])
