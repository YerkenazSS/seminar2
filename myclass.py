class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r=r
        self.g=g
        self.b=b

    def changecolor(self, red, green, blue):
        self.r=red
        self.g=green
        self.b=blue

    def calculate(self):
        print("Values of this color is r= ", self.r, "g= ", self.g, "b=", self.b)
