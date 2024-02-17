import random
from node import Node
from distance import Distance
from topology import Topology
from network import Network
import matplotlib.pyplot as plt

class TMAN:
    """
    Methods:
    - get_nodes(): Get the list of nodes.
    - get_network_directory(): Get the network directory.
    - calculate_total_node_distance(nodes): Calculate the sum of distances of neighboring nodes.
    - initialize_network(N, k): Initialize the network with nodes and random connections.
    - select_k_nearest_neighbors(node, neighbor_list, k): Select k nearest neighbors for a given node.
    - update_new_nearest_neighbors(node, old_neighbors, new_neighbors): Update nearest neighbors based on new connections.
    - evolve_topology(nodes): Perform the optimization of the network based on distance over a specified number of cycles.
    """

    # input handling
    topology_dict = {
        'ring': 'R',
        'spectacles': 'S'
    }

    def __init__(self, total_nodes, total_neighbors, topology='ring'):
            # CONSTANT - given with the homework statement
            self.NUM_OF_CYCLES = 40
            
            self.N = total_nodes
            self.k = total_neighbors
            self.topology = topology
            self.FILE_NAME = f'{self.topology_dict[topology]}_N{self.N}_k{self.k}'

            self.network = Network(self.N, self.k, self.topology)
            self.nodes = self.network.initialize_network()

    
    def get_nodes(self):
        return self.nodes

    def get_network_directory(self):
        return self.network.network_directory

    def calculate_total_node_distance(self, nodes):
        """
        Calculate the sum of distances of neighboring nodes during the initialization phase.

        Args:
        - nodes (list): List of Node objects.

        Returns:
        - sum_of_distances (float): Sum of distances.
        """
        sum_of_distances = 0
        network_nodes_dict = self.get_network_directory()
        for node in nodes:
            for neighbor_id in node.get_neighbor_list():
                neighbor = network_nodes_dict[neighbor_id]
                node_distance = Distance(node, neighbor, self.topology)
                sum_of_distances += node_distance.calculate_distance()
        return sum_of_distances

    def select_k_nearest_neighbors(self, node, neighbor_list):
        """
        Select k nearest neighbors for a given node.

        Args:
        - node (Node): The node for which neighbors are to be selected.
        - neighbor_list (list): List of potential neighbors.

        Returns:
        - k_nearest_neighbor_ids (list): List of IDs of the k nearest neighbors.
        """
        node_distances = {}
        network_nodes_dict = self.get_network_directory()
        for neighbor_id in neighbor_list:
            neighbor = network_nodes_dict[neighbor_id]
            node_distance = Distance(node, neighbor, self.topology)
            node_distances[neighbor_id] = node_distance.calculate_distance()

        sorted_neighbors = sorted(node_distances.items(), key=lambda x: x[1])
        k_nearest_neighbor_ids = [neighbor[0] for neighbor in sorted_neighbors[:self.k]]
        return k_nearest_neighbor_ids

    def update_new_nearest_neighbors(self, node, old_neighbors, new_neighbors):
        """
        Update nearest neighbors based on the gossip.

        Args:
        - node (Node): The node whose neighbors need to be updated.
        - old_neighbors (list): List of old neighbors.
        - new_neighbors (list): List of new neighbors.
        """
        unique_neighbors = list(set(old_neighbors + new_neighbors))
        k_nearest_neighbors = self.select_k_nearest_neighbors(node, unique_neighbors)
        node.update_neighbor_list(k_nearest_neighbors)

    def evolve_topology(self, nodes):
        for _ in range(1, self.NUM_OF_CYCLES+1):
            for node in nodes:
                neighbor_id = node.select_random_neighbor()
                # gossiping
                node_partial_view = [node.id] + [neighbor for neighbor in node.neighbors if neighbor != neighbor_id]
                
                network_nodes_dict = self.get_network_directory()
                neighbor = network_nodes_dict[neighbor_id]
                # gossiping
                neighbor_partial_view = [neighbor_id] + [neighbor for neighbor in neighbor.neighbors if neighbor != node.id]

                # update both node and its neighbor with each other's partial view
                self.update_new_nearest_neighbors(node, node.get_neighbor_list(), neighbor_partial_view)
                self.update_new_nearest_neighbors(neighbor, neighbor.get_neighbor_list(), node_partial_view)
                
            total_distance = self.calculate_total_node_distance(nodes)

            '''
            Record below parameters -
            1. Sum of distances after each cycle
            2. Each node with their list of neighbors 
            3. Node graph of the network
            '''
            # save cycle vs distance in a csv file
            with open(f"{self.FILE_NAME}.txt", "a") as f:
                f.write(f"{_},{total_distance}\n")

            if _ in [1, 5, 10, 15, self.NUM_OF_CYCLES]:
                # save the each node with their list of neighbors in the self.file_name.txt file
                with open(f"{self.FILE_NAME}_{_}.txt", "w") as f:
                    f.write("node_id,neighbors\n")
                    for node in nodes:
                        f.write(f"{node.id},{node.get_neighbor_list()}\n")
                plt.figure(figsize=(6, 6))
                plt.title(f'State After Network Evolution Cycle {_}')
                final_network_nodes_dict = self.get_network_directory()
                for node in nodes:
                    x, y = node.location
                    plt.scatter(x, y, c=node.color)
                    # print(node.get_neighbor_list())
                    for neighbor_id in node.get_neighbor_list():
                        neighbor = final_network_nodes_dict[neighbor_id]
                        x_neighbor, y_neighbor = neighbor.location
                        plt.plot([x, x_neighbor], [y, y_neighbor], 'k-')
                plt.savefig(f'{self.FILE_NAME}_{_}.png')
                plt.close()