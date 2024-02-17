from topology import Topology
import random
from node import Node

class Network:

    def __init__(self, total_nodes, total_neighbors, topology='ring'):
        self.N = total_nodes
        self.k = total_neighbors
        self.topology = topology
        # NODE_ID: NODE directory
        self.network_directory = {}

    def initialize_network(self):
        if self.topology == 'ring':
            nodes = self.initialize_ring_network()
        elif self.topology == 'spectacles':
            nodes = self.initialize_spectacles_network()
    
        return self.attach_neighbors(nodes)

    def initialize_ring_network(self):
        nodes = []
        colors = ['Red', 'Green', 'Blue']
        node_positions = Topology(self.N, 'ring').get_positions()
        for i in range(self.N):
            node_id = random.randint(0, 1000000)
            position = node_positions[i]
            color = colors[i % len(colors)]
            node = Node(node_id, color, position)
            self.network_directory[node_id] = node
            nodes.append(node)
        return nodes

    def initialize_spectacles_network(self):
        nodes = []
        node_positions = Topology(self.N, 'spectacles').get_positions()
        for i in range(self.N):
            node_id = random.randint(0, 1000000)
            position = node_positions[i]
            # all nodes are of the same color
            node = Node(node_id, 'black', position)
            self.network_directory[node_id] = node
            nodes.append(node)
        return nodes

    def attach_neighbors(self, nodes):
        # assign neighbors to each node
        for node in nodes:
            potential_neighbors = [n for n in nodes if n != node]
            neighbors = random.sample(potential_neighbors, self.k)
            neighbor_ids = [n.id for n in neighbors]
            node.update_neighbor_list(neighbor_ids)
        return nodes