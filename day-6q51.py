#polymorphism method overloading
'''class Cal:
    def add(a,b,c):
        return a+b+c
obj1=Cal
print(obj1.add(1,2,3))'''
#another method variable length arguments
'''class Cal:
    def add(self,*args):
        return sum(args)
#take inputs
obj1=Cal
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))'''

class Cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return(sum)
#take inputs
obj1=Cal
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))

