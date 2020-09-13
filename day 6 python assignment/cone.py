import math


class Cone:

    def __init__(self, radius, height, slant_height):
        self.r = radius
        self.h = height
        self.s = slant_height


    def volume(self):
        vol = (3.142 * self.r * self.r * self.h)/3
        print("the volume of given cone is : ", vol)


    def surface_area(self):
        area = (3.142 * self.r * self.s) + (3.142 * self.r * self.r)
        print("the Surface Area of given cone is : ", area)


res = Cone(5, 12, 13)
res.volume()
res.surface_area()
