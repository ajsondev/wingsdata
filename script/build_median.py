from util import (
    load_projects, load_project_data, get_weighted_median_vote,
    get_median_vote, format_number
)


def main(**kwargs):
    print('project-id,weighted-median,lower-half-avg')
    for proj in load_projects():
        data = load_project_data(proj['id'])
        wmed_forecast = get_weighted_median_vote(data['votes'])
        med_forecast = get_median_vote(data['votes'])
        print(':'.join((
            proj['id'],
            format_number(med_forecast),
            format_number(wmed_forecast),
        )))
