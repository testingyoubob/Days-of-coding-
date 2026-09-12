class Customer: 
    def __init__(self,name,city): 
        self.name = name
        self.city = city

    def greet(self):
        print("Hello " + self.name + "! ")


c1 = Customer("Sarah", "Atlanta")
c2 = Customer("Rob", "Florence")
c3 = Customer("Thomas", "Denver")

Customer = [c1, c2, c3]

for c in Customer:
    c.greet()
    print(c.name + "Live in " + c.city)

    