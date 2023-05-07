import requests
from bs4 import BeautifulSoup
import json

url = 'https://api.kufar.by/search-api/v1/search/rendered-paginated?ar=5&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6M30%3D&lang=ru&prn=17000&query=iphone&rgn=2&size=43'

request = requests.get(url).json()

print(request)

with open('iphones.json', 'w', encoding='utf-8') as f:
    json.dump(request, f, ensure_ascii=False, indent=4)