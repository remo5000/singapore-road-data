import urllib.request

def get_speed_limit(road_name):
    keywords = '+'.join(road_name.upper().split())
    url = f'https://www.onemotoring.com.sg/content/onemotoring/en/on_the_roads/road_safety/speed_limits.html?keyword={keywords}'
    html = urllib.request.urlopen(url).read()
    print(html)
