from pprint import pprint
from util import load_projects

from weightedstats import weighted_median

from project.database import db


def main(**kwargs):
    ether = (10 ** 18)
    for proj in load_projects():
        weights = []
        amounts = []
        for cast in db.forecast.find({'project_addr': proj['address']}):
            weights.append(int(cast['raw']['lockedAmount']) / ether)
            amounts.append(int(cast['raw']['amount']) / ether)
        wmed = weighted_median(amounts, weights=weights)
        wmed_str = str(round(wmed / 1000, 1)).rstrip('0').rstrip('.')
        print('%s:%s' % (proj['name'], '%sk' % wmed_str))
