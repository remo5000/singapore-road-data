import overpy as op
import sys
from gmplot import gmplot
from road_point import RoadPoint
from output_text import export_road_points

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

# Generate pure coordinates
coord_list = [(float(rp.lat), float(rp.lon)) for rp in road_points]

# Setting up the canvas size for the map
gmap = gmplot.GoogleMapPlotter(1.3068055, 103.8188261, 15)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*coord_list)
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=5, marker=False)

# Heatmap
gmap.heatmap(top_attraction_lats, top_attraction_lons)

# Render
gmap.draw("my_map.html")

