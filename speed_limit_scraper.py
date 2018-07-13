import requests

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
    text = response.text
    print(html)
