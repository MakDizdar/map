from osm_parser import get_default_parser
from store import NodeSet
import sys

def extract_osm_nodes(f_name):
    # Parse the supplied OSM file
    print("Loading data...")
    parser = get_default_parser(f_name)
    node_set = NodeSet()
    for node in parser.iter_nodes():
        node_set.add(float(node['id']), float(node['lat']), float(node['lon']))
    return node_set

def select_nodes_in_rectangle(nodes, min_lat,max_lat, min_lng, max_lng):
    # actual min and max latitude and longitude of coordinates
    nodes_in_rectangle = NodeSet()
    for k, node in nodes.get_nodes().items():
        nodlat= float(node.lat)
        nodlng = float(node.lng)
        if(min_lat <= nodlat and nodlat <= max_lat and 
           min_lng <= nodlng and nodlng <= max_lng):
            nodes_in_rectangle.add(k, nodlat, nodlng)

    return nodes_in_rectangle


def print_rectangle(filename, min_lat,max_lat, min_lng, max_lng):
    all_nodes = extract_osm_nodes(filename)
    nodes_selected = select_nodes_in_rectangle(all_nodes, min_lat, max_lat, min_lng , max_lng)
    print(nodes_selected.print_node_set())

#print_rectangle("osmmap.osm",58.3697,58.4333,15.5733,15.576) 
