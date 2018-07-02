import overpy as op
from gmplot import gmplot

# Get API
api = op.Overpass()

# Query
query = "".join(l for l in open('query.xml'))
result = api.query(query)

# Generate plot from points
coord_list = [(float(n.lat), float(n.lon)) for n in result.nodes]
gmap = gmplot.GoogleMapPlotter(1.3068055, 103.8188261, 100)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*coord_list)
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=5, marker=False)

# Draw
gmap.draw("my_map.html")

