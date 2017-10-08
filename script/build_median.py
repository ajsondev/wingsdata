from pprint import pprint

from weightedstats import weighted_median

from project.database import db
from util import load_projects, load_forecast_data


def format_number(val):
    if val > 1000000:
        return '%sm' % str(round(val / 1000000, 1)).rstrip('0').rstrip('.')
    else:
        return '%sk' % str(round(val / 1000, 1)).rstrip('0').rstrip('.')


def main(**kwargs):
    ether = (10 ** 18)
    for proj in load_projects():
        weights = []
        amounts = []
        for cast in load_forecast_data(proj['id']):
            weights.append(int(cast['lockedAmount']) / ether)
            amounts.append(int(cast['amount']) / ether)
        wmed = weighted_median(amounts, weights=weights)
        print('%s:%s' % (proj['id'], format_number(wmed)))
