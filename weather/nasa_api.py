import webbrowser
import requests
import json


API_KEY = '4ramvdXfdpIOFglu7eMD6ksMOzGjdUeMdXxcSccB'

url = 'https://api.nasa.gov/planetary/apod'

params = {
     'api_key': API_KEY,
     'hd': 'True',
     'date': ''
}

response = requests.get(url, params=params)
json_data = json.loads(response.text)
image_url = json_data['url']

print(image_url)
