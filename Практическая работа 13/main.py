class Sphere():
    """Объект сфера(с радиусом и координатой центра)"""
    def __init__(self, r=0, x=0, y=0, z=0):
        self.r = float(r)
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        self.volum = (4/3) * 3.14 * self.r**3
        return self.volum

    def get_square(self):
        self.square = 4 * 3.14 * self.r ** 2
        return self.square

    def get_radius(self):
        return self.r

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, r):
        self.r = r
        return self.r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return self.x, self.y, self.z

    def is_point_inside(self, x, y, z):
        if (self.x - self.r < x < self.x + self.r) and (self.y - self.r < y < self.y + self.r) and (
                self.z - self.r < z < self.z + self.r):
            return True
        else:
            return False

s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print(s0.get_volume()) # 0.523598775598
print(s0.is_point_inside(0 , -1.5, 0)) # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6
