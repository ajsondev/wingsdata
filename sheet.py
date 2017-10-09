from pprint import pprint

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
SPREADSHEET_ID = '1R3uG31f5TZmSko4bQhEzdyRbp0fAgJnIfoaIg5QbJwE'


def init_gc():
    scope = [SCOPE]
    cred = ServiceAccountCredentials.from_json_keyfile_name('var/config.json', scope)
    gc = gspread.authorize(cred)
    return gc


def get_sheet():
    gc = init_gc()
    return gc.open_by_key(SPREADSHEET_ID).worksheet('ico')

def main():
    sheet = get_sheet()
    pprint(sheet.range('A3:B4'))


if __name__ == '__main__':
    main()
