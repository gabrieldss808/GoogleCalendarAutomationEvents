from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class CalendarAPI():

    scopes = ['https://www.googleapis.com/auth/calendar']
    credentials = None
    service = None

    def authenticate(self):

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.credentials = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scopes)
                self.credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.credentials, token)

        self.service = build('calendar', 'v3', credentials=self.credentials)

    def createEvent(self,title="",location="",description="",start="",end="",recurrence="",attendees=[],organizer=""):

        event = {
            'summary': title,
            'location': location,
            'description': description,
            "creator": { 
                "email": organizer,
            },
            'start': {
                'dateTime': start,#'2021-01-20T09:00:00-07:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': end,#'2021-01-20T17:00:00-07:00',
                'timeZone': 'America/Sao_Paulo',
            },
            # 'recurrence': [
            #     recurrence#'RRULE:FREQ=DAILY;COUNT=2'
            # ],
            "organizer": {
                "email": organizer,
            },
            'attendees': [
                attendees
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        #{'email': 'gabrieldss808@gmail.com'},
        #{'email': 'gabriel.ssouza@totvs'},

        try:

            event = self.service.events().insert(calendarId='gabrieldss808@gmail.com', body=event).execute()
        except Exception as e:

            print(e)

        print("")