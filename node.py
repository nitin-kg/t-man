import random 

class Node:
    def __init__(self, id, color, location, type='ring'):
        self.id = id
        self.location = location
        self._neighbors = []
        self.color = color
        # spectacles nodes don't need rgb color value
        if type == 'ring':
            self.rgb_color = self.calculate_color_value(color)

    def select_random_neighbor(self):
        return random.choice(self.get_neighbor_list())

    def update_neighbor_list(self, new_neighbors):
        self.neighbors = new_neighbors

    def get_neighbor_list(self):
        return self.neighbors

    # for Ring nodes
    def calculate_rgb_to_xyz(self):
        r1, g1, b1 = self.rgb_color

        r1 = r1 / 255
        g1 = g1 / 255
        b1 = b1 / 255

        if r1 > 0.04045:
            r1 = ((r1 + 0.055) / 1.055) ** 2.4
        else:
            r1 = r1 / 12.92
        if g1 > 0.04045:
            g1 = ((g1 + 0.055) / 1.055) ** 2.4
        else:
            g1 = g1 / 12.92
        if b1 > 0.04045:
            b1 = ((b1 + 0.055) / 1.055) ** 2.4
        else:
            b1 = b1 / 12.92

        r1 = r1 * 100
        g1 = g1 * 100
        b1 = b1 * 100

        x1 = r1 * 0.4124 + g1 * 0.3576 + b1 * 0.1805
        y1 = r1 * 0.2126 + g1 * 0.7152 + b1 * 0.0722
        z1 = r1 * 0.0193 + g1 * 0.1192 + b1 * 0.9505

        return (x1, y1, z1)

    def calculate_xyz_to_lab(self, x, y, z):
        x = x / 95.047
        y = y / 100.000
        z = z / 108.883

        if x > 0.008856:
            x = x ** (1/3)
        else:
            x = (7.787 * x) + (16 / 116)
        if y > 0.008856:
            y = y ** (1/3)
        else:
            y = (7.787 * y) + (16 / 116)
        if z > 0.008856:
            z = z ** (1/3)
        else:
            z = (7.787 * z) + (16 / 116)

        l = (116 * y) - 16
        a = 500 * (x - y)
        b = 200 * (y - z)

        return (l, a, b)
    
    def calculate_color_value(self, color):
        major_color_intensity = random.randint(200, 255)
        minor_color_intensity_1 = random.randint(0, 80)
        minor_color_intensity_2 = random.randint(0, 80)
        
        rgb_value = ()
        # create RGB tuple based on the color value
        if color == 'Red':
            rgb_value = (major_color_intensity, minor_color_intensity_1, minor_color_intensity_2)
        elif color == 'Green':
            rgb_value = (minor_color_intensity_1, major_color_intensity, minor_color_intensity_2)
        elif color == 'Blue':
            rgb_value = (minor_color_intensity_1, minor_color_intensity_2, major_color_intensity)
        
        return rgb_value