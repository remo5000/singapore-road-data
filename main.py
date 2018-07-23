import overpy as op
import sys
from pathos.multiprocessing import ProcessingPool as Pool

from road_point import RoadPoint
from output_text import export_road_points
from output_scatter import make_gmap
from speed_limit_scraper import get_speed_limit

# Process a node and make it a roadpoint.
# Abstracted to enable concurrency for processing nodes.
def node_to_RoadPoint(node):
    lat = float(node.lat)
    lon = float(node.lon)
    road_name = way.tags.get('name')
    lane_count =  way.tags.get('lanes')
    speed_limit = get_speed_limit(road_name)
    rp = RoadPoint(node.id, lat, lon, road_name,\
        lane_count, speed_limit) 

# Get API
api = op.Overpass()

# Query
query = "".join(l for l in open('query.xml'))
result = api.query(query)

# Get ways (roads or part of roads) 
# which have road names and lane count.
# Note that if we exclude the filters, there are many more 
# ponits to process (or even just lane count).
all_ways = result.get_ways()
ways = [w for w in all_ways if 'name' in w.tags and 'lanes' in w.tags]

node_dict = {}
for way in ways:
    for node in way.nodes:
        node_dict[node.id] = node

unique_nodes = list(node_dict.values())
with Pool() as p:
    road_points = p.map(node_to_RoadPoint, unique_nodes)
    export_road_points(road_points)
    make_gmap(road_points)

