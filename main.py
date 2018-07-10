import overpy as op
import sys

from road_point import RoadPoint
from output_text import export_road_points
from output_scatter import make_gmap

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
        rp = RoadPoint(node.id, float(node.lat), float(node.lon), way.tags.get('name'), way.tags.get('lanes')) 
        d[node.id] = rp

road_points = list(d.values())

export_road_points(road_points)
make_gmap(road_points)
