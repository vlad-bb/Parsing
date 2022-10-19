from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from .spiders.price import main as parser

''' Скрипт для читання та запису данних в GoogleSheets'''

SAMPLE_RANGE_NAME = 'table!A3:H279'


class GoogleSheet:
    SPREADSHEET_ID = '1p0jxTLPNe7-wVZ1D-dtdfltWiSkhMAcKdZeYYjPlQVE'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google_sheets/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def get_values(self):
        try:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return
            return values

            # for index, row in enumerate(values):
            #     # print(f'Row {index} {row}')
            #     yield index, row
        except HttpError as err:
            print(err)

    def update_cell(self, range_cell, _values):
        try:
            data = [{
                'range': range_cell,
                'values': _values
            }]
            body = {
                'valueInputOption': 'USER_ENTERED',
                'data': data
            }
            result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                                      body=body).execute()
            print(f'Row {range_cell} update {_values}')
        except HttpError as err:
            print(err)


# def main():
#     gs = GoogleSheet()
#     table_value = gs.get_values()
#     for index, row in enumerate(table_value):
#         index += 1
#         ean_number = row[1]
#         link = row[5]
#         print(f'EAN {type(ean_number)} LINK {type(link)}')
#         if ean_number != '' and link != '9':
#             parser(ean_number, link)
#
#         # print(f'Row {index} {row}')
#         # range_cell = f'table!G{index}:H{index}'
#         # values = [['0.00', 'False']]
#         # gs.update_cell(range_cell, values)
#
#
# if __name__ == '__main__':
#     main()
