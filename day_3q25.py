#reverse an array without using built in functions
arr=[12,21,31,41]
rev=""
n=0
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(str(rev)) 