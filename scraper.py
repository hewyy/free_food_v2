import json
import requests

def get_events():
	# list of keywords that lead to the food not being free
	banned_words = ['Oxford Housing','Bursley Hall','South Quad','South Quadrangle','North Quad','North Quadrangle','East Quad','East Quadrangle','Mosher-Jordan Hall', "Mary Markley Hall"]
	url = "https://events.umich.edu/week/json?filter=tags%3AFood%2C&v=1"
	print(url)

	#acceses the page from the url
	client = requests.get(url)

	#this formats the page correctly
	page_json = json.loads(client.text)

	#print(page_json)

	events = []
	#saving parsed data in a list
	for eye_dee in page_json:
		temp = page_json[eye_dee]
		if temp["location_name"] in banned_words or temp["event_title"] in banned_words:
			continue
		else:
			start = {"dateTime":temp["date_start"]+"T"+temp["time_start"]+"-04:00"}
			end = {"dateTime":temp["date_end"]+"T"+temp["time_end"]+"-04:00"}
			
			if(len(end["dateTime"]) != 25):
				end = start
			event = {"summary":temp["event_title"], "location":temp["location_name"], "description":temp["permalink"],"start":start, "end":end}
			events.append(event)

	return events