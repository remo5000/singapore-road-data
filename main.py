import overpy as op

# Get API
api = op.Overpass()

# Read custom query from xml file
query = "".join(l for l in open('query.xml'))
result = api.query(query)
print(len(result.nodes))
