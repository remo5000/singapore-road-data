from gmplot import gmplot

# Takes in a list of RoadPoints and outputs a gmap file.
def make_gmap(road_points):
    # Generate pure coordinates
    coord_list = [(float(rp.lat), float(rp.lon)) for rp in road_points]

    # Setting up the canvas size for the map
    gmap = gmplot.GoogleMapPlotter(1.3068055, 103.8188261, 15)

    # Scatter points
    top_attraction_lats, top_attraction_lons = zip(*coord_list)
    gmap.scatter(top_attraction_lats, top_attraction_lons,\
        '#3B0B39', size=5, marker=False)

    # Heatmap
    gmap.heatmap(top_attraction_lats, top_attraction_lons)

    # Render
    gmap.draw("my_map.html")

