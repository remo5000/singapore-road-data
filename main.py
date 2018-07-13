import overpy as op
import sys

from road_point import RoadPoint
from output_text import export_road_points
from output_scatter import make_gmap
from speed_limit_scraper import get_speed_limit

# Get API
api = op.Overpass()

# Query
query = "".join(l for l in open('query.xml'))
result = api.query(query)

# Get ways (roads or part of roads) with road names 
all_ways = result.get_ways()
ways = [w for w in all_ways if 'name' in w.tags and 'lanes' in w.tags]
d = {}
for way in ways:
    for node in way.nodes:
        lat = float(node.lat)
        lon = float(node.lon)
        road_name = way.tags.get('name')
        lane_count =  way.tags.get('lanes')
        rp = RoadPoint(node.id, lat, lon, road_name,\
            lane_count, get_speed_limit(road_name)) 
        d[node.id] = rp

road_points = list(d.values())

export_road_points(road_points)
make_gmap(road_points)
