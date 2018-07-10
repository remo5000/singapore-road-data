import overpy as op
import sys
from gmplot import gmplot

class RoadPoint:
    # lat:float lon:float roadname:string lane_count:int
    def __init__(self, node_id, lat, lon, road_name, lane_count):
        self.node_id = node_id
        self.lat = lat
        self.lon = lon
        self.road_name = road_name
        self.lane_count = lane_count

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
# Clear file
open("coordinates.txt", "w")
for rp in road_points:
    print(f'Lat: {rp.lat}, Lon: {rp.lon}, Road name: {rp.road_name}, Number of lanes: {rp.lane_count}', file=open("coordinates.txt", "a+"))

# Generate pure coordinates
coord_list = [(float(rp.lat), float(rp.lon)) for rp in road_points]

# This part has been left out, as there is no need to visualise.
gmap = gmplot.GoogleMapPlotter(1.3068055, 103.8188261, 15)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*coord_list)
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=5, marker=False)

# Heatmap
gmap.heatmap(top_attraction_lats, top_attraction_lons)

# Render
gmap.draw("my_map.html")

