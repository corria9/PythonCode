class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("Im a duck! Quack!")

def feed_the_duck(thing):
    thing.quack()

feed_the_duck(Duck())                
feed_the_duck(Person())