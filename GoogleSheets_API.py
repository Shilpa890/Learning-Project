#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from __future__ import print_function

import os.path
import pandas as pd

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
# from main.index import print_sheet

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1-GGTWLdEw8Ucj2uXmQSEqmMJHLcRSV6DTdJZEh80va0'
SAMPLE_SHEET = ['AgentData','TeamData','SalaryData']
Agent_df = pd.DataFrame()
Team_df = pd.DataFrame()
Salary_df = pd.DataFrame()
DF_MAP = dict()
DF_MAP['AgentData'] = Agent_df
DF_MAP['TeamData'] = Team_df
DF_MAP['SalaryData'] = Salary_df




def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../secrets/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        #print(len(SAMPLE_SHEET))
        tb = []
        dfs=[]
        for _sheet in SAMPLE_SHEET:

            #print(SAMPLE_SHEET[r])
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=_sheet).execute()
            values = result.get('values', [])
            DF_MAP[_sheet] = pd.DataFrame(values[1:],columns=values[0])
            print('setting df {}'.format(_sheet))
            #print(tb[r])
            #print(values)
        #print(tb[0])
        if not values:
            print('No data found.')
            return

        #print('Name, Major:')
        # for row in values:
        #     # Print columns A and E, which correspond to indices 0 and 4.
        #     print('%s, %s %s' % (row[0], row[1], row[2]))
    except HttpError as err:
        print(err)
    return DF_MAP


if __name__ == '__main__':
    main()