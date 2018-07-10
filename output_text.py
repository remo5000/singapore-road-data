# Takes in an array of RoadPoints and 
# outputs information into a text file.
def export_road_points(road_points):
    # Clear file
    open("coordinates.txt", "w")
    for rp in road_points:
        print(f'Lat: {rp.lat}, Lon: {rp.lon}, Road name: {rp.road_name}, Number of lanes: {rp.lane_count}', file=open("coordinates.txt", "a+"))

