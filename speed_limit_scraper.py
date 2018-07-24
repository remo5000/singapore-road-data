import requests
from bs4 import BeautifulSoup

# Returns speed limit of a given road name in string format.
# Scrapes ONE.MOTORIN website
# Invalid/failed response returns empty string
def get_speed_limit(road_name):
    keywords = '+'.join(road_name.upper().split())
    url = f'https://www.onemotoring.com.sg/content/onemotoring/en/on_the_roads/road_safety/speed_limits.html?keyword={keywords}'
    # html = urllib.request.urlopen(url).read()
    response = requests.get(url)
    if response.status_code != 200:
        return '' 
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')
    limit = soup.find('div', {"class": "gridtable"}).find('div', {"class": "row"}).find('div',  {"class": "cell cell30 textleft"}).find('p').contents[0]
    print('Speed limit at ' + road_name + ': ' + limit)
    return limit
