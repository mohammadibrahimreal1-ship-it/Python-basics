class Animal:                   #Superclass or Parentclass
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speak Now...")

# e1 = Animal("Bruno")
# e1.speak()


class Dog(Animal):              #Dog is an subclass which inherits class Animal

    def speak(self):
        super().speak()         #super means using function(method) of super class... here, it somewhat says "I want to execute/use 'speak' method from superclass"
        print("Woof!")

d = Dog("Bruno")
d.speak()
print(d.location)