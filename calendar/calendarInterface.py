from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#----------------------------------------------------------------------------#
#                                 SETUP                                      #
#----------------------------------------------------------------------------#

# If modifying these scopes, delete the file token.pickle.
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

#----------------------------------------------------------------------------#
#                             EVENT FUNCTIONS                                #
#----------------------------------------------------------------------------#
#               note: these are alogirithmically identical to assignment
#                     functions. they simply do not distinctify themselves
#                     in the calendar as "[ASSIGNMENT]"

# prints the names and start times of the next 10 events on user's calendar
# code idea and algorithm from Google APIs
def getEvents():
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])   

getEvents() 

# returns the next event on the calendar
def getNextEvent():
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])   
    
#name a string for the name of the assignment
#date a string for the date the assignment is due, without time information:
#   ex, no parenthesis: year-month-day
def addEvent(name, date):
    # events must have a start and end time. In order for events to be logged as 
    # a single day and not a certain time, the event needs to go from 00:00 to 24:00.
    event = {
        'summary': name,
        'start': {             
            # day-long event, so that each assignment appears in the top pane of your calendar with the due date:
            'dateTime': date+"T00:00:00-05:00",
            'timeZone':'America/New_York'
        },
        'end': {
            'dateTime': date+"T22:00:00-07:00",
            'timeZone':'America/New_York'
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created.')

#----------------------------------------------------------------------------#
#                          ASSIGNMENT FUNCTIONS                             #
#----------------------------------------------------------------------------#

def getAssignments():
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=20, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])   

year = "2021"
month = "03"

# user inputs year, month, day, and then we default the time to a "day long" event. Thus, time will always be the same:

time = year+'-'+month+'-'+"11" #day

addEvent("Assignment 4 for WebDev", time)
