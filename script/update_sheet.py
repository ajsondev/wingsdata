from datetime import datetime
from sheet import get_sheet
from util import (
    load_projects, load_project_data, get_weighted_median_vote,
    get_median_vote, get_weight_sum, format_number
)


def main(**kwargs):
    sheet = get_sheet()
    assert sheet.acell('K2').value.strip() == 'Median'
    assert sheet.acell('L2').value.strip() == 'Weighted Median'
    assert sheet.acell('P2').value.strip() == 'Wings Used'
    rownum = 2
    for proj in list(load_projects()):
        rownum += 1
        data = load_project_data(proj['id'])
        median = get_median_vote(data['votes'])
        wmedian = get_weighted_median_vote(data['votes'])
        weight_sum = get_weight_sum(data['votes'])
        assert sheet.cell(rownum, 1).value.strip() == proj['name']
        sheet.update_acell('K%d' % rownum, '%s' % format_number(median))
        sheet.update_acell('L%d' % rownum, '%s' % format_number(wmedian))
        sheet.update_acell('P%d' % rownum, '%s' % format_number(weight_sum))
    ts = datetime.utcnow().strftime('%d %b, %H:%M UTC')
    sheet.update_acell('A1', ts)
