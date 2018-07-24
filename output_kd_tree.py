from pickle import dumps, loads
from ast import literal_eval
from scipy.spatial import cKDTree as KDtree

# Takes in an array of road points and 
# Outputs a pickled kd-tree into the directory
def make_kdtree(road_points):
    coords = [(rp.lat, rp.lon) for rp in road_points] 
    tree = KDtree(coords)
    dumped = dumps(tree)
    open("kdtree.txt", "w")
    print(dumped, file=open("kdtree.txt", "a+"))
    return tree  

# Load a kd tree from kdtree.txt in the same directory.
def load_dumped_kdtree():
    dumped_file = open("kdtree.txt", "r")
    dumped = literal_eval(dumped_file.read())
    kdtree = loads(dumped)
    return kdtree

