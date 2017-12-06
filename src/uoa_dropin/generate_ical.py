import icalendar

def generate_ical(events):

    cal = icalendar.Calendar()

    for event in events:

        ical_event = icalendar.Event()

        ical_event.add('summary', event['name'])
        ical_event.add('dtstart', event['start'])
        ical_event.add('dtend', event['end'])
        ical_event.add('uid', event['id'])

        cal.add_component(ical_event)
    
    return cal.to_ical()
