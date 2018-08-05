# Singapore Road data

## Objectives
- To build evenly-spread geospatial data along Singapore roads
- To get as much road data as possible (lanes, etc.)

## Usage
- install `overpy` and `gmplot` using pip
- run `python3 main.py`
- open the generated `my_map.html`.
- run `python3 -i load.py` to get a REPL with a 
  1. kd-tree of coordinates
  2. dictionary of coordinates mapping to `RoadPoint`s

