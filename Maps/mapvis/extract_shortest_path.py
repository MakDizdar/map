from extract_edges import *
from extract_nodes import extract_osm_nodes
from store import Node
import heapq

#from priodict import priorityDictionary

#noder = extract_osm_nodes("osmmap.osm")
#kanter = extract_osm_ways("osmmap.osm")
#edge_set = update_edgeset_weights(kanter,noder)
#graph = extract_graph_alt(edge_set)
#graph1 = extract_graph(edge_set)

# def get_ways_from_node(Graph, node):
#     edges_from_node = list()
#     for v in Graph[node]:
#         edges_from_node.append((v,Graph[node][v]))
#     return edges_from_node


   
# #Compare_weight not used anymore
# def compare_weight(Graph, start):
#     """Sorts a list of tuples where first elemnt of 
#     tuple is a node and the second element is the weight.
#     Returns the node of the first element that has the
#     cheapest weight"""
#     edges_from_node = get_ways_from_node(Graph, start)
#     sorted_edges = []
#     while edges_from_node:
#         a = edges_from_node[0]
#         for x in edges_from_node:
#             if x[1] < a[1]:
#                 a = x
#             sorted_edges.append(a)
#             edges_from_node.remove(a)
#     return sorted_edges[0][0]

def shortestPath(graph, start, end):
    """Given the input is a graph,'check extract_graph_alt'
    this function will calculate the shortestPath between start 
    and end where start and end  is the node_id of the start node 
    respectively end node"""
    queue=[(0, start, [])]
    visited=set()
    while True:
        if len(queue) == 0:
            return None
        (cost, v, path) = heapq.heappop(queue)
        if v not in visited:
            path = path + [v]
            visited.add(v)
            if v == end:
                return cost, path

            for (next,c) in graph[v]:
                heapq.heappush(queue, (cost + c , next, path))




def find_node(lat, lng, node_set):
    """Finds the node in the OSM-data that is
    nearest to the marked node using length_haversine"""
    markednode = Node('0000', lat, lng)
    iter_node_set = node_set.get_nodes()
    queue=[]
    for node in iter_node_set:
        node_class = iter_node_set[node]
        length = length_haversine(markednode, node_class)
        heapq.heappush(queue, (length, node_class))        
    return heapq.heappop(queue)
        





#TEST CASES BELOW, IGNORE

#58.40941788217388 lat
#15.56286334991455 lng
#find_node(58.426482468181455, 15.530462265014648, noder)

#short = shortestPath(graph, '1100534282', '1100534517')
#short2 = shortestPath(graph, '100168', '1533033365' )
#short3 = shortestPath(graph, '450586942','1414041761')
#short4 = shortestPath(graph, '26970457' , '1422532270')
#short5 = shortestPath(graph, '135091' , '264505')
#short6 = shortestPath(graph, '3676178799', '264526')
#short7 = shortestPath(graph, '1073862193', '274242389')
#short8 = shortestPath(graph, '80759' , '1322685027')


        
#queue = [(+,start,[])]     
#  heappush...
#    (12, "1337", [start])
#    queue = [(0, start, []), (12, "1337", [start]) (13, "42", [])]
#'1414008801': ['1414008816', '1414008792', '1414008816', '1414008792']
