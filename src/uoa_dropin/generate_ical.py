import icalendar
import pytz

def generate_ical(events):

    cal = icalendar.Calendar()

    for event in events:

        ical_event = icalendar.Event()

        event['start'] = event['start'].astimezone(pytz.timezone('America/Edmonton'))
        event['end'] = event['end'].astimezone(pytz.timezone('America/Edmonton'))

        ical_event.add('summary', event['name'])
        ical_event.add('dtstart', event['start'])
        ical_event.add('dtend', event['end'])
        ical_event.add('uid', event['id'])

        cal.add_component(ical_event)
    
    return cal.to_ical()
