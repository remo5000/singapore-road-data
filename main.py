import overpy as op
import sys
# from pathos.multiprocessing import ProcessingPool as Pool
import concurrent.futures

from road_point import RoadPoint
from output_text import export_road_points
from output_scatter import make_gmap
from output_kd_tree import make_kdtree
from speed_limit_scraper import get_speed_limit

# Process a road point and add a speed limit property.
# Abstracted to enable concurrency for processing nodes.
def append_speed_limit(road_point):
    road_point.speed_limit = get_speed_limit(road_point.road_name)
    return road_point

# Converts a node to a RoadPoint, without speed_limit
# This is done to prevent overloading in the multiprocessing
# step with the large overpy node object.
def node_to_RoadPoint(node):
    lat = float(node.lat)
    lon = float(node.lon)
    road_name = way.tags.get('name')
    lane_count =  way.tags.get('lanes')
    return RoadPoint(node.id, lat, lon, road_name, lane_count) 

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

# Remove duplicates in nodes (e.g 2 connected ways sharing a node)
node_dict = {}
for way in ways:
    for node in way.nodes:
        node_dict[node.id] = node

unique_nodes = list(node_dict.values())
road_points_without_speedlimit = [node_to_RoadPoint(n) for n in unique_nodes]

executor = concurrent.futures.ThreadPoolExecutor()
road_points = list(executor.map(append_speed_limit, road_points_without_speedlimit))
print("done processing all points!")
export_road_points(road_points)
kdtree = make_kdtree(road_points)
make_gmap(road_points)

