import click
import icalendar
import arrow

from .get_calendar import get_calendar, DANCE_ID
from .generate_ical import generate_ical


@click.command()
@click.option('--calendar-id', help='ID of the calendar to get', 
              default=DANCE_ID)
@click.option('--month', help='The month')
@click.option('--output-file', help='The output will be written to this file '
              'or stdout if no file is specified')
def main(calendar_id, month, output_file):

    uoa_events = get_calendar(calendar_id, month)

    events = [{
        'id': e['EventId'],
        'start': arrow.get(e['StartDate']).datetime,
        'end': arrow.get(e['EndDate']).datetime,
        'name': e['Title']
    } for e in uoa_events]

    ical = generate_ical(events)

    if output_file:
        with open(output_file, 'wb') as f:
            f.write(ical)
    else:

        lines = ical.split(sep=b'\r\n')

        for line in lines:
            print(line.decode('ASCII'))

main()
