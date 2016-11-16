class Node:
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat
        self.lng = lng

class NodeSet:
    def __init__(self):
        self.nodes = dict()

        # actual min and max latitude and longitude of coordinates
        self.bounds = dict()
        self.bounds["min_lat"] = 90
        self.bounds["max_lat"] = -90
        self.bounds["min_lng"] = 180
        self.bounds["max_lng"] = -180

    def add(self, id, lat, lng):
        self.nodes[id] = Node(id, lat, lng)
        self.bounds["min_lat"] = min(self.bounds["min_lat"], lat)
        self.bounds["min_lng"] = min(self.bounds["min_lng"], lng)
        self.bounds["max_lat"] = max(self.bounds["max_lat"], lat)
        self.bounds["max_lng"] = max(self.bounds["max_lng"], lng)

    def remove(self, id):
        del self.nodes[id]

    def get_nodes(self):
        return self.nodes

    def print_node_set(self):
        for k, n in self.nodes.items():
            print("id:" + str(k) + "\tlat: " + str(n.lat) +
                  "\tlng:" + str(n.lng))

class Edge:
    def __init__(self, f, t, weight = None):  #f och t ar noder i relation till varandra
        self.f = f
        self.t = t
        self.weight = weight
    def print_edge(self):
        print(str(self.f) + ":" + str(self.t))
    
    def update_weight(self, weight):
        if self.weight is None:
            self.weight = weight
        else:
            self.weight = min(weight, self.weight)

class EdgeSet:
    def __init__(self):
        self.edges = dict()
    def add(self, f, t, weight):
        self.edges[(f,t)] = Edge(f,t, weight)
    def add_road(self, r):
        self.edges.add(r)
    def get_edges(self):
        return self.edges
    def print_edge_set(self):
        print(self.edges)

    
