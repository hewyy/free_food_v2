import datetime
import pickle
import os.path
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def upload(events):
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            
    service = build('calendar', 'v3', credentials=creds)

    
    #delete all the events
    ids = open('events.txt', 'r')
    eye_dee = ids.readline()
    while eye_dee:
        time.sleep(0.1)
        service.events().delete(calendarId='primary', eventId=eye_dee.replace('\n', '')).execute()
        eye_dee = ids.readline()
    ids.close()


    #create new events
    ids = open('events.txt', 'w')   
    for event in events:
        #if its not already in the calander
        ev = service.events().insert(calendarId='primary', body=event).execute()
        print(ev["id"], file=ids)
        print("Event created")
        time.sleep(.300)