import urllib2
import json


## converts a list to string
def convert_to_urlstring(element_list):
	string_url = ''
	for e in element_list:
		if isinstance(e,str):
			string_url += e
		else:
			string_url += str(e)
		string_url += '/'
	return string_url[:-1] # we don't want / at the end of the string

zip_code = input('Enter zip code: ')
query = [zip_code]
api_key = '2d70303b01f33a3c'
feature = ['forecast'] 

# store the url in url_string
url_string = 'http://api.wunderground.com/api/' + api_key + '/' + convert_to_urlstring(feature) + '/q/' + convert_to_urlstring(query) +'.json'

#opening the file and loading it as json

f = urllib2.urlopen(url_string)
weather_file = json.loads(f.read())

print weather_file