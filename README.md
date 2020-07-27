# free_food_v2
better version of the free food web scrapping script

## Prerequisites
- [google calendar API](https://developers.google.com/calendar)
- Python 3.7 (or better)

## What the code does
1. request JSON file from umich events webpage
      - https://events.umich.edu/week/json?filter=tags%3AFood%2C&v=1
2. parse the file for free food events
3. reformat parsed data into a format recognized by the google calendar API
4. create a list of the reformatted event objects
5. validate google API credentials using the following files:
      - credentials.json
      - token.pickle
6. delete all previously created events in the events.txt file to prevent duplicates
7. using the list of event objects, add the events to google calendar using the google calendar API
8. save the added event id's to the event.txt file so that they can be deleted


## Event Objects
Event objects are used to store all the data required for each event.
They are formated in the following way:

{'summary': **Add event title**, 'location': **Add event location**, 'description': **Add link to events page**, 'start': {'dateTime': **start time (ISO 8601 TimeDate format)**}, 'end': {'dateTime': **end time (ISO 8601 TimeDate format)**}}




