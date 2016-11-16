import random
import unittest

from store import Node, NodeSet
from extract_nodes import select_nodes_in_rectangle 
from extract_nodes import extract_osm_nodes


def node_inside(node, min_lat, max_lat, min_lng, max_lng):
    return (min_lat <= node.lat and node.lat <= max_lat and 
            min_lng <= node.lng and node.lng <= max_lng)

class TestSelectNodes(unittest.TestCase):
    def test_empty_nodes(self):
        nodes = NodeSet()
        selected_nodes = select_nodes_in_rectangle(nodes, -10, 10, -10, 10)
        self.assertEqual(nodes.nodes, selected_nodes.nodes)

    def test_empty_clip_nodes(self):
        nodes = NodeSet()
        nodes.add(1, -10, -10)
        nodes.add(2, -5, -5)

        selected_nodes = select_nodes_in_rectangle(nodes, 0, 10, 0, 10)
        self.assertFalse(selected_nodes.nodes)

    def test_some_nodes_inside(self):
        nodes = NodeSet()
        nodes.add(1, -4, -2)
        nodes.add(2, -3, -2)
        selected_nodes = select_nodes_in_rectangle(nodes,-4,4 , -4,4)
        self.assertTrue(len(nodes.nodes.keys()) >= 1)
    def test_all_nodes_inside(self):
        nodes = NodeSet()
        nodes.add(1, -10, -10)
        nodes.add(2, -5, -5)
        selected_nodes = select_nodes_in_rectangle(nodes, -10, 10, -10 ,10)
        
        self.assertTrue(nodes.nodes.keys() == selected_nodes.nodes.keys())

    def test_random(self):
        # Create 100 random nodes
        nodes = NodeSet()
        for i in range(100):
            nodes.add(i, random.randint(-180, 180), 
                      random.randint(-90, 90))

        # Randomly choose the min and max latitude and longitude
        min_lat = random.randint(-90, 90)
        min_lng = random.randint(-180, 180)
        max_lat = min_lat + random.randint(0, 90-min_lat)
        max_lng = min_lng + random.randint(0, 180-min_lng)
        
        # Extract all nodes within the randomly generated rectangle
        selected_nodes = select_nodes_in_rectangle(nodes, min_lat, max_lat, 
                                                   min_lng, max_lng)

        # Make sure that all nodes that should be inside are inside
        for n in nodes.nodes.values():
            if n.id in selected_nodes.nodes.keys():
                self.assertTrue(node_inside(n, min_lat, max_lat, 
                                            min_lng, max_lng))
            else:
                self.assertFalse(node_inside(n, min_lat, max_lat, 
                                             min_lng, max_lng))

if __name__ == '__main__':
    unittest.main()
