from osm_parser import get_default_parser
from store import EdgeSet
from math import sqrt, radians , sin ,cos, asin
from extract_nodes import *


import sys

def extract_osm_ways(f_name):
    """Extracts all edges from the osm
    where the edge is represented as startnode and endnode"""
    print("Loading data..")
    parser = get_default_parser(f_name)
    edge_set = EdgeSet()
    for way in parser.iter_ways():
        if 'highway' in way['tags']:
            for node in way['road']:
                pos = way['road'].index(node)
                if pos+1 < len(way['road']):
                    endedge=way['road'][pos+1]
                    edge_set.add(node, endedge, None)
                    edge_set.add(endedge,node,None)
            #edge_set.add(way['road'][node],way[road'][node+1], None)
            #edge_set.add(way['road'][node+1],way['road'][node], None)
    print("Done!")
    return edge_set


def extract_graph_alt(edge_set):
    """Given that edge_set is an edgeset with updated_weights,
    extracts a graph that is represented as a dictionary where 
    a key is the node id and the key value is a list of tuples, 
    first element of the tuple is the neighbour and second is the
    weight of the edge"""
    print("Loading data...")
    adjlist = dict()
    for edge in edge_set:
        if not edge[0] in adjlist:
            if not edge[1] in adjlist:
               adjlist[edge[0]] = [(edge[1], edge_set[(edge[0],edge[1])].weight )]
               adjlist[edge[1]] = [(edge[0], edge_set[(edge[1],edge[0])].weight )]
            else:
                adjlist[edge[0]] = [(edge[1], edge_set[(edge[0],edge[1])].weight)]
                adjlist[edge[1]].append((edge[0], edge_set[( edge[1], edge[0] )].weight))

        else:
            if not edge[1] in adjlist:
                adjlist[edge[0]].append((edge[1], edge_set[(edge[0],edge[1])].weight))
                adjlist[edge[1]]= [(edge[0], edge_set[(edge[1],edge[0])].weight)]
            else:
                adjlist[edge[0]].append((edge[1], edge_set[(edge[0],edge[1])].weight))
                adjlist[edge[1]].append((edge[0], edge_set[(edge[1],edge[0])].weight))
    print("Done!")
    return adjlist

   

def length_haversine(p1, p2):
    # calculate the distance between two points using the Haversine
    # formula which incorporates the earth's curvature, see
    # http://en.wikipedia.org/wiki/Haversine_formula.
    lat1 = p1.lat
    lng1 = p1.lng
    lat2 = p2.lat
    lng2 = p2.lng
    lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))
    # return the distance in m
    return 6372797.560856 * c

def update_edgeset_weights(edgeset,nodeset):
    """Updates the weights of every edge in a edgeset
    by returning the class value of every node in
    nodeset"""
    iter_nodeset = nodeset.get_nodes()
    iter_edgeset = edgeset.get_edges()
    for edge in iter_edgeset:
        edge_node1= int(iter_edgeset[edge].f)
        edge_node2= int(iter_edgeset[edge].t)
        startnode = iter_nodeset[edge_node1]
        endnode = iter_nodeset[edge_node2]
        w =length_haversine(startnode,endnode)
        iter_edgeset[edge].update_weight(w)
    return iter_edgeset

#edge_set is for eample EdgeSet.get_edges() 
# def extract_adjacent_list(edge_set):
#     """Extracts an adjacent list for every node,
#     is not used anymore"""
#     print("Loading data...")
#     adjlist = dict()
#     for edge in edge_set:
#         if not edge[0] in adjlist:
#             if not edge[1] in adjlist:
#                adjlist[edge[0]] = [edge[1]]
#                adjlist[edge[1]] = [edge[0]]
#             else:
#                 adjlist[edge[0]] = [edge[1]]
#                 adjlist[edge[1]].append(edge[0])

#         else:
#             if not edge[1] in adjlist:
#                 adjlist[edge[0]].append(edge[1])
#                 adjlist[edge[1]]= [edge[0]]
#             else:
#                 adjlist[edge[0]].append(edge[1])
#                 adjlist[edge[1]].append(edge[0])
#     print("Done!")
#     return adjlist

# def extract_graph(edge_set):
#     """Extract all nodes and its neighbours with key value
#     in the inner dictionary is the weight between the edges.
#     This function is not used anymore"""
#     #edge_set is an edge_set that has edges with updated weights
#     adjlist = dict()
#     for edge in edge_set:
#         if not edge[0] in adjlist:
#             if not edge[1] in adjlist:
#                 adjlist[edge[0]] = {edge[1]:edge_set[(edge[0], edge[1])].weight}
#                 adjlist[edge[1]] = {edge[0]:edge_set[(edge[1],edge[0])].weight}
#         else:
#             if not edge[1] in adjlist:
#                 adjlist[edge[1]] = {edge[0]:edge_set[(edge[1],edge[0])].weight}
#                 adjlist[edge[0]][edge[1]] = edge_set[(edge[0],edge[1])].weight
#             else:
#                 adjlist[edge[0]][edge[1]] = edge_set[(edge[0], edge[1])].weight
#                 adjlist[edge[1]][edge[0]] = edge_set[(edge[1], edge[0])].weight
#     print("Done!")
#     return adjlist

#noder = extract_osm_nodes("osmmap.osm")
#kanter = extract_osm_ways("osmmap.osm")
#a =update_edgeset_weights(kanter,noder)
