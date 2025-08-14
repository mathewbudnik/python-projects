class car:
    def __init__(self, brand):
        self.brand = brand
        print(brand)

    def brake(self, dist):
        return dist + 50

    def honk(self):
        print("honk")

c = car("toyota")
#c.honk()
#print(c.brake(30))