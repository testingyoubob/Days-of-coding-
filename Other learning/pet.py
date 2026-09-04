class Dog:
    #1. SETUP: Runs once when you create a dog  
    def __init__(self, name,):
        self.name = name #Save the name inside this specific dog

    #2.ACTION: A function this dog can perform 
    def bark(self):
        print(f"{self.name} says Woof!")

#Using the Class

my_dog = Dog("Rex")

#Run the action 
my_dog.bark() #Output: Rex Says Woof! 
