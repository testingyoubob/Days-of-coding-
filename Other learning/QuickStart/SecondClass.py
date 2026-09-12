class Customer:
    def __init__(self, name , city):
        self.name = name 
        self.city = city 

    def __enter__(self): 
        print("Entering scope.")
        return self

    def __exit__(self, type, exc_value, traceback):
        print("Leaving scope")

    def greet(self):
        print("Hello " + self.name + "!")

with Customer ("Rob", "Florence") as robert:
    robert.greet()
    