import math

class Topology:

    def __init__(self, total_nodes, required_topology):
        self.total_nodes = total_nodes
        self.required_topology = required_topology

    def get_positions(self):
        # stragegy pattern
        if self.required_topology == 'ring':
            return self.ring()
        elif self.required_topology == 'spectacles':
            return self.spectacles()

    def ring(self):
        RADIUS = 100
        # You can choose how to place the N nodes on the plane relative to the origin. 
        # For example, a node location can be given by (𝑐𝑜𝑠𝜃, 𝑠𝑖𝑛𝜃) where 𝜃 is the length 
        # of the curve or angle relative to the positive x-axis in radians.
        node_positions = []
        for i in range(self.total_nodes):
            x = RADIUS * math.cos(2 * math.pi * i / self.total_nodes)
            y = RADIUS * math.sin(2 * math.pi * i / self.total_nodes)
            node_positions.append((x, y))
        return node_positions

    def spectacles(self):
        RADIUS = 100
        node_positions = []

        nodes_in_half_circle = self.total_nodes // 5
        # draw a circle
        nodes_in_circle = nodes_in_half_circle * 2

        # for each of the node we will calculate the x and y node_positions starting from left horizontal diagonal
        for i in range(nodes_in_circle):
            angle = 2 * math.pi * i / nodes_in_circle
            x = RADIUS * math.cos(angle)
            y = RADIUS * math.sin(angle)
            node_positions.append((x, y))

        # shift the x axis coordinate to the right by the radius and calculate coordinate for the half circle
        for i in range(nodes_in_half_circle):
            angle = math.pi * i / nodes_in_half_circle
            x = RADIUS * math.cos(angle) + 2 * RADIUS
            y = RADIUS * math.sin(angle)
            node_positions.append((x, y))

        # Generate node_positions for the second circle
        for i in range(nodes_in_circle):
            angle = 2 * math.pi * i / nodes_in_circle
            x = RADIUS * math.cos(angle) + RADIUS * 4
            y = RADIUS * math.sin(angle)
            node_positions.append((x, y))

        return node_positions
