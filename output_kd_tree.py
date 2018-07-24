from pickle import dumps
import kdtree

# Takes in an array of road points and 
# Outputs a pickled kd-tree into the directory.
def make_kdtree(road_points):
    coords = [(rp.lat, rp.lon) for rp in road_points]
    tree = kdtree.create(coords)
    dumped = dumps(tree)
    open("kdtree.txt", "w")
    print(dumped, file=open("kdtree.txt", "a+"))
    return tree  
