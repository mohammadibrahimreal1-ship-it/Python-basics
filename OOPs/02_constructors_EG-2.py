class Dog:

    def __init__(self, name, breed):    #Constructor and its parameters
        self.name = name
        self.breed = breed

    def my_doggy_name(self):
        return self.name
        
my_dog = Dog("Bella", "Poodle")
print(my_dog.my_doggy_name())