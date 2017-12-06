
import requests

API_URL = 'https://www.ualberta.ca/api/events/eventlist.json'

DANCE_ID ='B22987DF8410413993BECF1E337033F7'

def get_calendar(calendar_id, month):

    data = {
        'Calendars': [calendar_id],
        'Month': '2017-12'
    }

    r = requests.post(API_URL, data=data)

    if not r:
        print('Error: Cannot get the calendar.')
        return 1
    
    events = r.json()

    return events
