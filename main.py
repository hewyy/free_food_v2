from scraper import get_events
from calander import upload

events = get_events()
upload(events)
