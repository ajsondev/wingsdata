import json

from weightedstats import weighted_median


def load_projects():
    return json.load(open('data/project.json'))


def load_forecast_data(pid):
    return json.load(open(get_forecast_data_path(pid)))


def get_forecast_data_path(pid):
    return 'data/forecast/%s.json' % pid


def format_number(val):
    if val > 1000000:
        val = round(val / 1000000, 1)
        suffix = 'm'
    else:
        val = round(val / 1000, 1)
        suffix = 'k'
    return '%s%s' % (str(val).rstrip('0').rstrip('.'), suffix)


def load_project_data(pid):
    ether = (10 ** 18)
    votes = []
    for cast in load_forecast_data(pid):
        weight = int(cast['lockedAmount']) / float(ether)
        amount = int(cast['amount']) / float(ether)
        votes.append({
            'weight': weight,
            'amount': amount,
        })
    return {
        'votes': votes,
    }


def get_weighted_median_vote(votes):
    weights = [x['weight'] for x in votes]
    amounts = [x['amount'] for x in votes]
    return weighted_median(amounts, weights=weights)


def get_median_vote(votes):
    amounts = [x['amount'] for x in votes]
    return weighted_median(amounts)


def get_weight_sum(votes):
    weights = [x['weight'] for x in votes]
    return sum(weights)
