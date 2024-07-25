#write a code to demonstrate mutlilevel inheritance
class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
    def Bark():
        return "Bow..."
class puppy(Dog):
    def Bark():
        return  "Bow....."
obj1=Animal
obj2=Dog
obj3=puppy
print(obj2.speak())
print(obj2.Bark())
print(obj3.Bark())
