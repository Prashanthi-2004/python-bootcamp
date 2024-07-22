 #arthematic operations
a=int (input())
b=int (input())
print("sum of two numbers",a+b)
print("sub of two numbers",a-b)
print("mulp of two numbers",a*b)
print("division  of two numbers",a/b)
print("module of two numbers",a%b)
print("pow of a b",a*b) #this condition for the power condition #square we use as *
# logical operators it contain two conditions (AND,OR) if the both stmts are true we use AND,
# if one condition is false we use OR. 
age=int(input())
if (age>18 and age<24):
    print("two wheeler")
elif(age>=24 and age<45):
    print("two and four wheelers")
elif(age>+45):
    print("any vehicle")
    #example problem for conditions:
    total=700
apple=int(input())
banana=int(input())
orange=int(in put())
costapple=15
costbanana=4
costorg=5
tot=(total-(apple*costapple+banana*costbanana+orange*costorg))
if tot+total>total:
    print("cheated")
else:
    print("not cheated")
