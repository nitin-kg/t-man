
class Distance:

    def __init__(self, node1, node2, topology='ring'):
        self.node1 = node1
        self.node2 = node2
        if topology == 'ring':
            self.strategy = "color"
        else:
            self.strategy = "euclidean"

    def calculate_distance(self):
        if self.strategy == "euclidean":
            return self.calculate_euclidean_distance()
        elif self.strategy == "color":
            return self.calculate_color_distance()

    def calculate_color_distance(self):
        xyz1 = self.node1.calculate_rgb_to_xyz()
        x1, y1, z1 = xyz1
        xyz2 = self.node2.calculate_rgb_to_xyz()
        x2, y2, z2 = xyz2

        lab1 = self.node1.calculate_xyz_to_lab(x1,y1,z1)
        lab2 = self.node2.calculate_xyz_to_lab(x2,y2,z2)

        l1, a1, b1 = lab1
        l2, a2, b2 = lab2

        return ((l1 - l2) ** 2 + (a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5
        
    def calculate_euclidean_distance(self):
        x1, y1 = self.node1.location
        x2, y2 = self.node2.location

        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5