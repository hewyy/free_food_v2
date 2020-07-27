# free_food_v2
better version of the free food web scrapping script

## Prerequisites
- [google calendar API](https://developers.google.com/calendar)
- Python 3.7 (or better)

## How the works
1. request JSON file from umich events webpage
2. parse the file for free food events
3. reformat parsed data into a format recognized by the google calendar API
4. validate google API credentials using the following files:
      - credentials.json
      - token.pickle
