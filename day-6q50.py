#polymorphism method overiding
class Animal:
    def speak():
        return "Speaking...."
class Dog(Animal):
    def Speak():
        return "Dog is speaking....." 
class puppy(Dog):
    def speak():
        return "puppy is speaking....." 
obj3=puppy
print(obj3.speak()) 

#first run() is lost
'''def run():
    return "running"
def run():
    return "hello world"
print(run())'''
