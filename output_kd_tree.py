from pickle import dumps, loads
from ast import literal_eval
from scipy.spatial import cKDTree as KDtree
import sys

# Takes in an array of road points and 
# Outputs pickled forms of 
# 1) A kd-tree, with nodes as coordinates
# 2) A dictionary, mapping coordinates (lat, lon) to RoadPoints 
def make_kdtree(road_points):
    sys.setrecursionlimit(50000)
    coords = []
    dictionary = {}
    for rp in road_points:
        coords.append((rp.lat, rp.lon))
        dictionary[(rp.lat, rp.lon)] = rp
    tree = KDtree(coords)
    # Dump tree
    dumped = dumps(tree)
    open("kdtree.txt", "w")
    print(dumped, file=open("kdtree.txt", "a+"))
    # Dump dictionary
    dumped = dumps(dictionary)
    open("coords_to_roadpoints.txt", "w")
    print(dumped, file=open("coords_to_roadpoints.txt", "a+"))
    return tree  

# Load a kd tree from kdtree.txt in the same directory, as kdtree
def load_dumped_kdtree():
    dumped_file = open("kdtree.txt", "r")
    dumped = literal_eval(dumped_file.read())
    kdtree = loads(dumped)
    return kdtree

# Loads a dumped dictionary from coords_to_roadpoints.txt in 
# the same directory
def load_dumped_dictionary():
    dumped_file = open("coords_to_roadpoints.txt", "r")
    dumped = literal_eval(dumped_file.read())
    dictionary = loads(dumped)
    return dictionary
