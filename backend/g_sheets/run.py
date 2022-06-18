from distutils.command.build import build
from pprint import pprint
import os
from urllib import response

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# ID current Google Sheet
sheet_id = '1AZ44qofs3jX3WjIRVVQq9uAwZVd7N6voFKnq-6aNbSU'

# Auth
def get_service_sacc():
    creds_json = os.path.dirname(__file__) + '\creds.json'  #editor's key
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    creds_json,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http())
    return googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

#Get data from table
def get_sheet():
    return get_service_sacc().spreadsheets().values().get(spreadsheetId=sheet_id, range='A2:D5000').execute()

if '__main__' == __name__:
    pprint(get_sheet())
