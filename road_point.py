class RoadPoint:
    # lat:float lon:float roadname:string lane_count:int
    def __init__(self, node_id, lat, lon, road_name,\
            lane_count, speed_limit):
        self.node_id = node_id
        self.lat = lat
        self.lon = lon
        self.road_name = road_name
        self.lane_count = lane_count
        self.speed_limit = speed_limit

