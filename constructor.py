class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def showData(self):
        print("Vehicle Name:",self.name)
        print("Vehicle Color:",self.color)
        print("Vehicle price:",self.price)

    def start(self):
        print("Vehicle start with key")

    def fuel(self):
        print("Vehicle run with petrol and electric..")
    
v = Vehicle("Thar","black",400000.00)
v.showData()
v.start()
v.fuel()
