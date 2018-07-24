from pickle import dumps
from scipy.spatial import cKDTree as KDtree

# Takes in an array of road points and 
# Outputs a pickled kd-tree into the directory.
def make_kdtree(road_points):
    coords = []
    for rp in road_points:
        print(rp)
        coords.append((rp.lat, rp.lon))
    tree = KDtree(coords)
    dumped = dumps(tree)
    open("kdtree.txt", "w")
    print(dumped, file=open("kdtree.txt", "a+"))
    return tree  
